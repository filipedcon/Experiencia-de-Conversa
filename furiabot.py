from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN
from handlers.commands import start, furia
from handlers.messages import handle_message

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("furia", furia))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🔥 Bot da FURIA está rodando... Torcida, vamos com tudo! 🔥")
    app.run_polling()

if __name__ == "__main__":
    main()
