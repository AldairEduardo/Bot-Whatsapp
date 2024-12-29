from groq import Groq


def get_response(text):
    try:     

        client = Groq(
            api_key="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")

        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {"role": "system", "content": "Eres un asistente de IA. Recuerda dar respuestas concretas y precisas."},
                {"role": "user", "content": text}
            ],
            max_tokens=500,
            stream=False,
            temperature=0.7,

        )
        response = completion.choices[0].message.content
        return response

    except Exception as exception:
        print(exception)
        return "error"
    
# if __name__ == "__main__":
#     prompt_usuario = input("Escribe tu pregunta o mensaje: ")
#     respuesta = get_response(prompt_usuario)
#     print(f"Llama: {respuesta}")
