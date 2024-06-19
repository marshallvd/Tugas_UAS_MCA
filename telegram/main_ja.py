from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging
from db import Session, Inbox, Outbox, CeritaRakyat, QueryLog
from datetime import datetime
import queue
import threading

# Konfigurasi logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

session = Session()

# Enum untuk state aplikasi
class AppState:
    MAIN_MENU = 1
    STORY_LIST = 2
    SEARCH_STORY = 3 

# Antrian pesan global
message_queue = queue.Queue()

# Fungsi worker untuk memproses antrian pesan
def worker():
    while True:
        try:
            chat_id, message_handler, message = message_queue.get()
            message_handler(message)
            message_queue.task_done()
        except Exception as e:
            logger.error(f"Error processing message: {e}")

# Mulai thread worker
worker_thread = threading.Thread(target=worker, daemon=True)
worker_thread.start()

# Fungsi untuk memulai bot
async def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    logger.info(f"User {user.first_name} started the bot.")
    
    # Kirim pesan sapaan
    await update.message.reply_text('🇮🇩 Hai! Saya adalah Marbot\nChatbot Cerita Rakyat Indonesia Anda.')
    
    # Kirim pesan perkenalan menu
    await update.message.reply_text('Berikut merupakan beberapa cerita rakyat yang bisa saya ceritakan:')
    
    # Simpan state pengguna ke context
    context.user_data['state'] = AppState.MAIN_MENU
    
    # Kirim pesan menu
    await update.message.reply_text(get_menu_text(), parse_mode='Markdown')

def get_menu_text():
    return (
        '📜 *Menu Utama:*\n\n'
        '1️⃣ *Daftar Cerita Rakyat*\n'
        'Ketik "1" untuk melihat daftar cerita rakyat.\n\n'
        '2️⃣ *Cari Cerita Rakyat*\n'
        'Ketik "2" untuk mencari cerita rakyat.\n\n'
        '3️⃣ *Bantuan*\n'
        'Ketik "/help" untuk mendapatkan petunjuk penggunaan bot.'
    )

# Fungsi untuk memberikan bantuan kepada pengguna
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "🆘 *Bantuan*\n\n"
        "Untuk menggunakan bot ini, Anda dapat memilih dari menu utama:\n"
        "1. Ketik '1' untuk melihat daftar cerita rakyat.\n"
        "2. Ketik '2' untuk mencari cerita rakyat berdasarkan judul.\n"
        "3. Ketik '/help' untuk melihat pesan bantuan ini lagi."
    )

# Fungsi untuk mencari cerita berdasarkan judul yang mengandung penggalan judulnya
async def search_story_by_title(query_text, update, context):
    search_results = session.query(CeritaRakyat).filter(CeritaRakyat.judul.ilike(f'%{query_text}%')).all()

    if search_results:
        context.user_data['search_results'] = search_results

        response = '🔍 *Hasil Pencarian:*\n\n'
        for index, story in enumerate(search_results, start=1):
            response += f'{index}. {story.judul}\n'
        response += '\nKetik nomor cerita untuk membaca cerita selengkapnya.'

        await context.bot.send_message(chat_id=update.effective_chat.id, text=response, parse_mode='Markdown')

        # Set state ke STORY_LIST agar handle_story_selection bisa menangani pemilihan cerita
        context.user_data['state'] = AppState.STORY_LIST
    else:
        response = "Maaf, tidak ditemukan cerita dengan judul yang sesuai."
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

        # Kembalikan state ke MAIN_MENU
        context.user_data['state'] = AppState.MAIN_MENU
        await update.message.reply_text(get_menu_text(), parse_mode='Markdown')


# Fungsi untuk menangani pesan yang masuk
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    text = update.message.text.lower()

    logger.info(f"Received message from {update.message.from_user.first_name}: {text}")

    if 'state' not in context.user_data:
        context.user_data['state'] = AppState.MAIN_MENU
    
    state = context.user_data['state']

    if state == AppState.MAIN_MENU:
        if text == "1":
            context.user_data['state'] = AppState.STORY_LIST
            await show_story_list(user_id, update, context)
        elif text == "2":
            context.user_data['state'] = AppState.SEARCH_STORY
            await context.bot.send_message(chat_id=update.effective_chat.id, text="🔍 *Cari Cerita Rakyat*\n\nMasukkan penggalan judul cerita yang ingin Anda cari:", parse_mode='Markdown')
        elif text == "/help":
            await help_command(update, context)
        else:
            response = "Maaf, saya tidak mengerti permintaan Anda. Silakan pilih opsi dari menu utama."
            await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    elif state == AppState.STORY_LIST:
        await process_story_list(user_id, text, update, context)
    elif state == AppState.SEARCH_STORY:
        await search_story_by_title(text, update, context)
    else:
        response = "Maaf, saya tidak mengerti permintaan Anda. Silakan pilih opsi dari menu utama."
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)



async def handle_story_selection(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    text = update.message.text

    # Pastikan ada hasil pencarian tersedia di user_data
    if 'search_results' in context.user_data:
        search_results = context.user_data['search_results']

        try:
            # Memeriksa apakah input adalah nomor urut dalam daftar hasil pencarian
            selected_index = int(text) - 1

            if selected_index >= 0 and selected_index < len(search_results):
                selected_story = search_results[selected_index]
                await show_story_detail(selected_story.id, update, context)
            else:
                raise IndexError

        except (ValueError, IndexError):
            response = "Maaf, pilihan Anda tidak valid."
            await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

            # Kembalikan state ke MAIN_MENU
            context.user_data['state'] = AppState.MAIN_MENU
            await update.message.reply_text(get_menu_text(), parse_mode='Markdown')

    else:
        response = "Maaf, tidak ada hasil pencarian yang tersedia saat ini."
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

        # Kembalikan state ke MAIN_MENU
        context.user_data['state'] = AppState.MAIN_MENU
        await update.message.reply_text(get_menu_text(), parse_mode='Markdown')



async def show_story_detail(story_id, update, context):
    story = session.query(CeritaRakyat).filter_by(id=story_id).first()

    if story:
        response = f'🟢 *{story.judul}*\n\n{story.isi}'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response, parse_mode='Markdown')
    else:
        response = "Maaf, cerita yang Anda pilih tidak ditemukan."
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    context.user_data['state'] = AppState.MAIN_MENU
    await update.message.reply_text(get_menu_text(), parse_mode='Markdown')

async def process_story_list(user_id, text, update, context):
    if text.isdigit():
        try:
            story_id = int(text)
            await show_story_detail(story_id, update, context)
        except ValueError:
            response = "Maaf, cerita yang Anda pilih tidak ditemukan."
            await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    else:
        response = "Maaf, saya tidak mengerti permintaan Anda. Silakan pilih opsi dari menu utama."
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def show_story_list(user_id, update, context):
    stories = session.query(CeritaRakyat).all()

    if stories:
        response = '📜 *Daftar Cerita Rakyat:*\n\n'
        for index, story in enumerate(stories, start=1):
            response += f'{index}. {story.judul}\n'
        response += '\nKetik nomor atau judul cerita untuk membaca ceritanya.'
    else:
        response = "Tidak ada cerita rakyat yang ditemukan."

    outbox_message = Outbox(user_id=str(user_id), message=response)
    session.add(outbox_message)
    session.commit()

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response, parse_mode='Markdown')

def log_menu_selection(user_id):
    query_log = QueryLog(
        user_id=str(user_id),
        query_type='menu_selection',
        query='menu_selection',  # Atau nilai lain yang sesuai
        timestamp=datetime.utcnow()
    )
    session.add(query_log)
    session.commit()

def log_story_search(user_id, query_text):
    query_log = QueryLog(
        user_id=str(user_id),
        query_type='story_search',
        query=query_text,
        timestamp=datetime.utcnow()
    )
    session.add(query_log)
    session.commit()

def main() -> None:
    # Ganti 'YOUR_TOKEN_HERE' dengan token bot Anda
    application = Application.builder().token("6700492977:AAFWzFALx6HubjVg3-OolA2ENKzj_efrLXM").build()

    # Tambahkan handler untuk /start command
    application.add_handler(CommandHandler("start", start))

    # Tambahkan handler untuk /help command
    application.add_handler(CommandHandler("help", help_command))

    # Tambahkan handler untuk pesan teks
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Mulai polling
    application.run_polling()

if __name__ == '__main__':
    main()
