from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging
from db import Session, Inbox, Outbox, CeritaRakyat, QueryLog
from datetime import datetime

# Konfigurasi logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

session = Session()

# Enum untuk state aplikasi
class AppState:
    MAIN_MENU = 1
    STORY_LIST = 2

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

# Fungsi untuk menangani pesan yang masuk
async def handle_message(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    user_id = user.id
    text = update.message.text.lower()

    logger.info(f"Received message from {user.first_name}: {text}")

    # Memeriksa state pengguna
    if 'state' not in context.user_data:
        context.user_data['state'] = AppState.MAIN_MENU
    
    state = context.user_data['state']

    # Memproses teks pesan berdasarkan konteksnya
    if state == AppState.MAIN_MENU:
        if text == "1":
            context.user_data['state'] = AppState.STORY_LIST  # Update state ke STORY_LIST
            await show_story_list(user_id, update, context)
            log_menu_selection(user_id)
        elif text == "2":
            await context.bot.send_message(chat_id=update.effective_chat.id, text="🔍 *Cari Cerita Rakyat*\n\nMasukkan judul cerita yang ingin Anda cari:", parse_mode='Markdown')
        else:
            await process_main_menu(user_id, text, update, context)
    elif state == AppState.STORY_LIST:
        await process_story_list(user_id, text, update, context)
    
    # # Kirim menu utama jika tidak dalam STATE STORY_LIST
    # if state != AppState.STORY_LIST:
    #     await update.message.reply_text(get_menu_text(), parse_mode='Markdown')
    #     context.user_data['state'] = AppState.MAIN_MENU



async def process_main_menu(user_id, text, update, context):
    if text.isdigit() and text == "1":
        # Masuk ke state daftar cerita
        context.user_data['state'] = AppState.STORY_LIST
        await show_story_list(user_id, update, context)
        log_menu_selection(user_id)
    elif text == "/help":
        await help_command(update, context)
    else:
        response = "Maaf, saya tidak mengerti permintaan Anda. Silakan pilih opsi dari menu utama."
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def process_story_list(user_id, text, update, context):
    if text.isdigit():
        try:
            story_id = int(text)
            await show_story_detail(story_id, update, context)
        except ValueError:
            response = "Maaf, cerita yang Anda pilih tidak ditemukan."
            await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    else:
        await process_message(user_id, text, update, context)

async def show_story_list(user_id, update, context):
    # Menjalankan query untuk mendapatkan daftar cerita rakyat
    stories = session.query(CeritaRakyat).all()

    # Logika untuk menampilkan daftar cerita kepada pengguna
    if stories:
        response = '📜 *Daftar Cerita Rakyat:*\n\n'
        for index, story in enumerate(stories, start=1):
            response += f'{index}. {story.judul}\n'
        response += '\nKetik nomor atau judul cerita untuk membaca ceritanya.'
    else:
        response = "Tidak ada cerita rakyat yang ditemukan."

    # Simpan respon ke tb_outbox
    outbox_message = Outbox(user_id=str(user_id), message=response)
    session.add(outbox_message)
    session.commit()

    # Kirim respon ke pengguna
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response, parse_mode='Markdown')


async def show_story_detail(story_id, update, context):
    story = session.query(CeritaRakyat).filter_by(id=story_id).first()
    if story:
        response = f'🟢 *{story.judul}*\n\n{story.isi}'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response, parse_mode='Markdown')
    else:
        response = "Maaf, cerita yang Anda pilih tidak ditemukan."
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        return
    
    # Setelah menampilkan cerita, kembalikan state pengguna ke MAIN_MENU
    context.user_data['state'] = AppState.MAIN_MENU
    
    # Kirim menu utama seperti pada saat /start
    await update.message.reply_text(get_menu_text(), parse_mode='Markdown')


def log_menu_selection(user_id):
    query_log = QueryLog(
        user_id=str(user_id),
        query_type='menu_selection',
        query='menu_selection'  # Atau nilai lain yang sesuai
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
