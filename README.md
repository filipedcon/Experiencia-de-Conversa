# 🐾 Bot da FURIA CS — Telegram 

🔥 Um bot interativo para os fãs da **FURIA Esports**!  
Torça, interaja, acompanhe os jogos **ao vivo**, veja o elenco atualizado e troque ideia com uma IA que fala como a torcida raiz! 🇧🇷🐾

---

## ✨ O que esse bot faz?

Este bot foi feito para rodar no Telegram e oferece:

- 📋 **Elenco atualizado** do time de CS2 da FURIA
- 🟢 **Status ao vivo dos jogos** com placar
- 🎙️ **Gritos de torcida simulados** (tipo: "É balaaaaaa!")
- 🤖 **Conversa com IA** no estilo fanático da torcida
- 🧠 IA integrada com o **Gemini 2.0 Flash** da Google

---

## 💻 Requisitos antes de começar

Você vai precisar de:

1. **Python instalado** (versão 3.10 ou superior)
   - [Download do Python](https://www.python.org/downloads/)

2. **Conta no Google** para gerar uma chave da IA (Gemini):
   - Acesse: [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Clique em “Create API Key” e copie a chave gerada

3. **Bot criado no Telegram**:
   - No Telegram, procure por `@BotFather`
   - Envie `/newbot` e siga as instruções
   - Pegue o token do seu bot

---

## 1. Faça a cópia do projeto

Utilize o git clone ou o botão de download para baixar o projeto no seu sistema.

## 2. Instale as dependências

pip install -r requirements.txt

## 3. Crie o arquivo .env com suas chaves

Crie um arquivo chamado .env na raiz do projeto ou um config.py e adicione:

TELEGRAM_BOT_TOKEN=coloque_aqui_o_token_do_seu_bot_do_telegram
GEMINI_API_KEY=coloque_aqui_sua_api_key_do_google

## 4. Execute o bot

python main.py

---

### 📌 To-do (Futuras Melhorias)

1. Notificações automáticas dos jogos
2. Ranking interativo dos jogadores
3. Painel com estatísticas em tempo real
