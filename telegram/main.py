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
    await update.message.reply_text(
        'Halo! Saya adalah chatbot Anda. Berikut beberapa hal yang bisa saya lakukan:\n\n'
        '1. Pantun\n'
        'Ketik "pantun" untuk mendapatkan pantun.\n\n'
        '2. Jokes\n'
        'Ketik "jokes" untuk mendapatkan lelucon.\n\n'
        '3. Menyapa\n'
        'Ketik "halo" atau "hai" untuk menyapa saya.\n\n'
        '4. Tanya Kabar\n'
        'Ketik "apa kabar" atau "bagaimana kabarmu" untuk menanyakan kabar saya.\n\n'
        '5. Nama\n'
        'Ketik "siapa namamu" untuk mengetahui nama saya.\n\n'
        '6. Bantuan\n'
        'Ketik "bantuan" untuk mendapatkan bantuan.'
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
    if "halo" in text or "hai" in text:
        response = "Halo! Ada yang bisa saya bantu?"
    elif "apa kabar" in text or "bagaimana kabarmu" in text:
        response = "Saya hanyalah bot, jadi saya selalu baik! Ada yang bisa saya bantu?"
    elif "siapa namamu" in text:
        response = "Nama saya adalah Chatbot, asisten virtual Anda."
    elif "bantuan" in text:
        response = "Tentu! Bagaimana saya bisa membantu Anda hari ini?"
    elif "pantun" in text:
        response = (
            "Ini dia pantun untuk Anda:\n\n"
            "Jalan-jalan ke Kota Blitar,\n"
            "Jangan lupa beli suvenir.\n"
            "Hai teman yang pintar,\n"
            "Tetaplah rajin belajar dan berpikir."
        )
    elif "jokes" in text:
        response = (
            "Berikut adalah sebuah lelucon untuk Anda:\n\n"
            "Kenapa sepeda tidak bisa berdiri sendiri?\n"
            "Karena sepeda hanya punya dua ‘roda’ (rida)!"
        )
    else:
        response = "Maaf, saya tidak mengerti. Bisa tolong ulangi?"

    # Simpan respon ke tb_outbox
    outbox_message = Outbox(user_id=str(user_id), message=response)
    session.add(outbox_message)
    session.commit()

    # Kirim respon ke pengguna
    await update.message.reply_text(response)

def main() -> None:
    # Ganti 'YOUR_TOKEN_HERE' dengan token bot Anda
    application = Application.builder().token("6700492977:AAFWzFALx6HubjVg3-OolA2ENKzj_efrLXM").build()

    # Tambahkan handler untuk /start command
    application.add_handler(CommandHandler("start", start))

    # Tambahkan handler untuk pesan teks
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Mulai polling
    application.run_polling()

if __name__ == '__main__':
    main()
