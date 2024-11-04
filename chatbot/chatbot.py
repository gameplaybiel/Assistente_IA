# Packages
import nltk
import random

# Baixar pacotes do NLTK (faça isso uma vez)
nltk.download('punkt')   # Para a tokenização de palavras
nltk.download('wordnet')  # Para a lematização

# Base de perguntas e respostas
answer = {
    "olá": ["Olá, como posso te ajudar?", "Olá! Em que posso te ajudar?"],
    "como você está": ["Estou bem, obrigado. E você?", "Se precisar de algo, eu estou aqui."],
    "como você está?": ["Estou bem, obrigado. E você?", "Se precisar de algo, eu estou aqui."],
    "qual é seu nome": ["Sou um chatbot para atendimento"],
    "qual é seu nome?": ["Sou Assistente IA, um chatbot para atendimento"],
    "até mais": ["Até logo!! Estarei aqui se você precisar. ", "Até a próxima!! Volte quando precisar!"]
}

# Função para a resposta
def chatbot_answer(question):
    question = question.lower().strip().rstrip("?")
    if question in answer:
        return random.choice(answer[question])
    else:
        return "Desculpe, não entendi. Você pode reformular a frase?"

print("Chatbot: Olá, digite pra sair.")
while True:
    user_input = input("Você: ")
    if user_input.lower() == "até mais":
        print("Chatbot: Até logo!")
        break
    response = chatbot_answer(user_input)
    print(f"Chatbot: {response}")