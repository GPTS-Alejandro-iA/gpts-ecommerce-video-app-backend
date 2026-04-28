import os
from groq import Groq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

async def generate_campaign_brain(payload: dict):
    prompt = payload.get("prompt", "Escribe una respuesta creativa.")

    try:
        response = client.chat.completions.create(
          model="llama3-groq-70b-tool-use-preview",
            messages=[
                {"role": "system", "content": "Eres un experto en marketing, ventas y energía solar."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return {
            "status": "ok",
            "prompt_enviado": prompt,
            "respuesta": response.choices[0].message["content"]
        }

    except Exception as e:
        return {
            "status": "error",
            "details": str(e)
        }





