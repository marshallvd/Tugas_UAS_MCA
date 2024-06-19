from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging
from sqlalchemy.orm import sessionmaker
from db import Session, Inbox, Outbox

# Konfigurasi logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

session = Session()

# Fungsi untuk memulai bot
async def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    logger.info(f"User {user.first_name} started the bot.")
    
    # Kirim pesan sapaan
    await update.message.reply_text('🇮🇩 Hai! Saya adalah Marbot\nChatbot Cerita Rakyat Indonesia Anda.')
    
    # Kirim pesan perkenalan menu
    await update.message.reply_text('Berikut merupakan beberapa cerita rakyat yang bisa saya ceritakan:')
    
    # Kirim pesan menu
    await update.message.reply_text(get_menu_text())

def get_menu_text():
    return (
        '📜 *Menu Cerita Rakyat:*\n\n'
        '1️⃣ *Malin Kundang*\n'
        'Ketik "malin kundang" untuk mendapatkan ceritanya.\n\n'
        '2️⃣ *Sangkuriang*\n'
        'Ketik "sangkuriang" untuk mendapatkan ceritanya.\n\n'
        '3️⃣ *Bawang Merah Bawang Putih*\n'
        'Ketik "bawang merah bawang putih" untuk mendapatkan ceritanya.\n\n'
        '4️⃣ *Timun Mas*\n'
        'Ketik "timun mas" untuk mendapatkan ceritanya.\n\n'
        '5️⃣ *Legenda Danau Toba*\n'
        'Ketik "danau toba" untuk mendapatkan ceritanya.\n\n'
        '6️⃣ *Bantuan*\n'
        'Ketik "/help" untuk mendapatkan petunjuk penggunaan bot.'
    )

# Fungsi untuk memberikan bantuan kepada pengguna
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "🆘 *Bantuan*\n\n"
        "Untuk mendapatkan cerita rakyat, ketik judul cerita yang ingin Anda dengar dengan huruf kecil, contohnya:\n"
        "➡️ malin kundang\n"
        "➡️ sangkuriang\n"
        "➡️ bawang merah bawang putih\n"
        "➡️ timun mas\n"
        "➡️ danau toba\n\n"
        "Atau Anda bisa memilih dari menu yang sudah tersedia."
    )

# Fungsi untuk menangani pesan yang masuk
async def handle_message(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    user_id = user.id
    text = update.message.text.lower()  # Convert the message to lowercase for easier comparison

    # Simpan pesan ke tb_inbox
    inbox_message = Inbox(user_id=str(user_id), message=text)
    session.add(inbox_message)
    session.commit()

    logger.info(f"Received message from {user.first_name}: {text}")

    # Logika respon chatbot
    if "malin kundang" in text:
        response = (
            "🟢 *Malin Kundang*\n\n"
            "🔹 *Cerita Singkat:*\n"
            "Malin Kundang adalah anak durhaka yang dikutuk menjadi batu oleh ibunya karena tidak mengakui ibunya setelah menjadi kaya. "
            "Cerita ini mengajarkan pentingnya berbakti kepada orang tua dan akibat dari durhaka."
        )
    elif "sangkuriang" in text:
        response = (
            "🟢 *Sangkuriang*\n\n"
            "🔹 *Cerita Singkat:*\n"
            "Sangkuriang jatuh cinta kepada Dayang Sumbi yang ternyata adalah ibunya sendiri. "
            "Setelah mengetahui kebenaran ini, Dayang Sumbi mengajukan syarat mustahil untuk menolak lamaran Sangkuriang. "
            "Cerita ini mengisahkan asal usul Gunung Tangkuban Perahu."
        )
    elif "bawang merah bawang putih" in text:
        response = (
            "🟢 *Bawang Merah Bawang Putih*\n\n"
            "🔹 *Cerita Singkat:*\n"
            "Bawang Putih adalah anak yang baik hati yang selalu diperlakukan tidak adil oleh ibu tiri dan saudara tirinya, Bawang Merah. "
            "Namun, kebaikan hati Bawang Putih akhirnya membawa kebahagiaan dan keberuntungan bagi dirinya."
        )
    elif "timun mas" in text:
        response = (
            "🟢 *Timun Mas*\n\n"
            "🔹 *Cerita Singkat:*\n"
            "Timun Mas adalah seorang gadis yang lahir dari timun emas yang diberikan oleh raksasa kepada sepasang suami istri. "
            "Untuk menghindari raksasa yang ingin memakannya, Timun Mas menggunakan benda-benda ajaib untuk melarikan diri."
        )
    elif "danau toba" in text:
        response = (
            "🟢 *Legenda Danau Toba*\n\n"
            "🔹 *Cerita Singkat:*\n"
            "Legenda ini mengisahkan seorang nelayan yang menikahi seorang putri ikan dan memiliki anak bernama Samosir. "
            "Karena melanggar janji untuk tidak memberitahukan asal usul istrinya, sang istri kembali menjadi ikan dan terbentuklah Danau Toba."
        )
    else:
        response = "Maaf, saya tidak mengerti. Bisa tolong ulangi? ❓"

    # Simpan respon ke tb_outbox
    outbox_message = Outbox(user_id=str(user_id), message=response)
    session.add(outbox_message)
    session.commit()

    # Kirim respon ke pengguna
    await update.message.reply_text(response)
    # Kirim menu kembali ke pengguna
    await update.message.reply_text(get_menu_text())

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
