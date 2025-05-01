from telegram import Update
from telegram.ext import ContextTypes
from services.ia import perguntar_para_ia
import random

# Elenco Atual da FURIA
players = {
    "yuurih": "Yuri Boian",
    "KSCERATO": "Kaike Cerato",
    "FalleN": "Gabriel Toledo",
    "molodoy": "Danil Golubenko",
    "YEKINDAR": "Mareks Gaļinskis (stand-in)",
    "Coach": "Sidnei Macedo"
}

# Status ao Vivo dos jogos
live_status = {
    "FURIA vs Team A": "Vitória da FURIA! (16x12)",
    "FURIA vs Team B": "Jogo em andamento... (8x7 no 1º half)"
}

# Reações da torcida
torcida_reactions = [
    "GO FURIAAAA! 🔥",
    "É NOSSO esse mapa! 🐾",
    "Confia na call do FalleN! 🎯",
    "Vamos yuurih! Vamos KSCERATO!"
]

# Função de tratamento de mensagens
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Elenco da FURIA
    if "elenco" in text:
        elenco = "\n".join(f"- {nick}: {name}" for nick, name in players.items())
        await update.message.reply_text(f"🎮 Elenco Atual da FURIA CS:\n{elenco}")

    # Status ao vivo dos jogos
    elif "status" in text:
        status = "\n\n".join(f"{jogo}: {resultado}" for jogo, resultado in live_status.items())
        await update.message.reply_text(f"📊 Status Ao Vivo:\n{status}")

    # Reação da torcida
    elif "torcida" in text:
        reaction = random.choice(torcida_reactions)
        await update.message.reply_text(f"🏟️ Torcida: {reaction}")

    # Informações sobre a FURIA
    elif "sobre" in text:
        sobre = (
            "A FURIA é uma das maiores organizações de esports do Brasil! 🇧🇷\n"
            "Fundada em 2017, participa de CS2, Valorant, Rocket League, entre outros.\n"
            "Filosofia: Competitividade, Inovação e Cultura! 🐾"
        )
        await update.message.reply_text(sobre)

    # Perguntas gerais
    else:
        resposta = await perguntar_para_ia(update.message.text)
        await update.message.reply_text(resposta)
