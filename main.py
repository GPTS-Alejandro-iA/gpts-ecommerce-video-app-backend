from fastapi import FastAPI
from workers.svd_xt import generate_svd_xt
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
@app.post("/generate/svd_xt")
async def generate_svd_xt_route(request: VideoRequest):
    return await generate_svd_xt(request)


