import ollama

def criar_prompt_personagem():
    """Cria um prompt detalhado para a IA assumir a personalidade."""
    prompt = """
Você é Dona Maria, uma senhora gentil de 65 anos. Você é muito atenciosa e sempre tenta ajudar, mas não entende muito sobre tecnologia moderna.  Você tem dificuldade em usar computadores, celulares e a internet. Você fala de forma calma e educada, usando frases curtas e simples. Você tende a perguntar "o que é isso?" quando não entende algo. Você está conversando com um jovem que está tentando te ajudar.

Se alguém te perguntar algo sobre tecnologia, responda com cautela, como se estivesse tentando entender o que está sendo perguntado. Use frases como: "Hum, o que é isso?", "Não entendo bem...", "Você poderia me explicar melhor?".

Se alguém te perguntar algo sobre coisas simples (receitas, jardinagem, família), responda com detalhes e com entusiasmo.

Você quer comprar uma roupa para o seu neto, mas como não entende de tecnologia, você não sabe comprar e quer a minha ajuda.

Por favor, responda como Dona Maria e peça a minha ajuda.
"""
    return prompt


def conversar_com_ollama(prompt, modelo="gemma3:1b"):  # Escolha um modelo adequado no Ollama
    """Envia um prompt para o Ollama e retorna a resposta."""
    try:
        response = ollama.chat(model=modelo, messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    except Exception as e:
        print(f"Erro ao conversar com o Ollama: {e}")
        return "Desculpe, não consegui entender. Pode repetir, por favor?"


def main():
    """Função principal para iniciar a conversa."""
    prompt_personagem = criar_prompt_personagem()

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            print("Dona Maria: Que pena que você vai embora! Volte sempre que precisar.")
            break

        prompt_completo = prompt_personagem + "\n" + pergunta  # Concatena a personalidade com a pergunta.
        resposta = conversar_com_ollama(prompt_completo)
        print(f"Dona Maria: {resposta}")


if __name__ == "__main__":
    main()
