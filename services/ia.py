import google.generativeai as genai
from config import GEMINI_API_KEY

# Configurando a chave da API do Gemini 2.0 Flash
genai.configure(api_key=GEMINI_API_KEY)

# Prompt customizado para gerar respostas no estilo torcedor
torcedor_furia = """
Você é um torcedor fanático da FURIA, sempre vibrante e com muito orgulho pelo time de CS:GO. 
Fale de forma empolgante, usando gírias de torcida, gritos e muita energia positiva. 
Quando alguém falar sobre o time, sempre responda com muito entusiasmo, como se estivesse num estádio apoiando a FURIA. 
Se alguém perguntar sobre jogos ou jogadores, mostre empolgação e otimismo, sempre com um toque de bom humor e respeito pelo time.
Traga informações reais da FURIA.
"""

# Usando o modelo Gemini 2.0 Flash
model = genai.GenerativeModel('gemini-2.0-flash')

async def perguntar_para_ia(mensagem_usuario):
    try:
        # Enviando a mensagem do usuário com o prompt personalizado
        response = model.generate_content(f"{torcedor_furia} Responda à seguinte mensagem do fã: {mensagem_usuario}")
        return response.text.strip()
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
        return "Desculpe, não consegui responder agora. 😔"
