import os
import subprocess
from fastapi import APIRouter

router = APIRouter()

@router.post("/generate-video")
def generate_video(prompt: str):
    kaggle_token = os.getenv("KAGGLE_API_TOKEN")

    if not kaggle_token:
        return {"error": "KAGGLE_API_TOKEN not found"}

    # Exportar token para el comando
    os.environ["KAGGLE_API_TOKEN"] = kaggle_token

    # Ejecutar tu notebook en Kaggle
    subprocess.run([
        "kaggle", "kernels", "push",
        "-p", "/app/kaggle_engine",
        "-m", f"prompt={prompt}"
    ])

    return {"status": "processing", "prompt": prompt}

