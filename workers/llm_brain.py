import os
from huggingface_hub import InferenceClient

HF_API_KEY = os.getenv("HF_API_KEY")

# Cliente oficial de HuggingFace
client = InferenceClient(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    token=HF_API_KEY
)


async def generate_campaign_brain(payload: dict):
    prompt = payload.get("prompt", "Escribe una respuesta creativa.")

    try:
        response = client.text_generation(
            prompt,
            max_new_tokens=300,
            temperature=0.7
        )

        return {
            "status": "ok",
            "prompt_enviado": prompt,
            "respuesta": response
        }

    except Exception as e:
        return {
            "status": "error",
            "details": str(e)
        }



