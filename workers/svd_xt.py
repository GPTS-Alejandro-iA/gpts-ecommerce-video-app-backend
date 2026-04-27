import requests
import base64
import uuid
import os

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

MODEL_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-video-diffusion-img2vid-xt"

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
    "Accept": "application/json"
}

async def generate_svd_xt(payload):
    """
    payload = {
        "prompt": str,
        "num_frames": int,
        "seed": int (optional)
    }
    """

    data = {
        "inputs": payload.prompt,
        "parameters": {
            "num_frames": payload.num_frames,
            "seed": payload.seed if payload.seed else None
        }
    }

    response = requests.post(MODEL_URL, headers=headers, json=data)

    if response.status_code != 200:
        return {"error": response.text}

    result = response.json()

    # HuggingFace devuelve el video en base64
    video_base64 = result.get("video")

    if not video_base64:
        return {"error": "No video returned from SVD-XT"}

    # Guardar el archivo temporalmente
    video_bytes = base64.b64decode(video_base64)
    filename = f"svdxt_{uuid.uuid4()}.mp4"

    with open(filename, "wb") as f:
        f.write(video_bytes)

    return {
        "filename": filename,
        "message": "SVD-XT video generated successfully"
    }

