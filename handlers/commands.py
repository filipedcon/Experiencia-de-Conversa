from telegram import Update
from telegram.ext import ContextTypes

# Comando de início
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Olá, torcedor! Seja bem-vindo ao chat oficial da FURIA! Mande sua mensagem e sinta a energia da nossa torcida!")

# Comando de informações (pode ser usado para outras interações, se necessário)
async def furia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("A FURIA é o melhor time de CS do Brasil! Vamos juntos em busca da vitória! 💛🖤")

