from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class VideoRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/generate-video")
def generate_video(request: VideoRequest):
    # Aquí va tu lógica real de generación de video
    # Por ahora devolvemos algo simple para probar
    return {
        "message": "Video generado correctamente",
        "prompt_recibido": request.prompt
    }


