import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")

LLAMA_MODEL = "meta-llama/Llama-3.1-8B-Instruct"

async def generate_campaign_brain(payload: dict):
    prompt = payload.get("prompt", "Escribe una respuesta creativa.")

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7
        }
    }

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{LLAMA_MODEL}",
        headers=headers,
        json=data
    )

    if response.status_code != 200:
        return {
            "status": "error",
            "details": response.text
        }

    result = response.json()

    return {
        "status": "ok",
        "model": LLAMA_MODEL,
        "prompt_enviado": prompt,
        "respuesta": result[0]["generated_text"]
    }


