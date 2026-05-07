from fastapi import FastAPI
from workers.svd_xt import generate_svd_xt
from workers.llm_brain import generate_campaign_brain
from pydantic import BaseModel
from groq import Groq
import os
from fastapi import UploadFile, File

@app.post("/kaggle-engine")
async def receive_kaggle_video(file: UploadFile = File(...)):
    # Guardar el archivo temporalmente
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Aquí luego puedes subirlo a Cloudflare R2 o S3
    # Por ahora devolvemos confirmación
    return {
        "status": "ok",
        "filename": file.filename,
        "message": "Video recibido correctamente"
    }

# TEMPORAL: imprimir modelos disponibles
try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    models = client.models.list()
    print(">>> MODELOS DISPONIBLES EN GROQ <<<")
    for m in models.data:
        print(" -", m.id)
    print(">>> FIN DE LISTA <<<")
except Exception as e:
    print(">>> ERROR LISTANDO MODELOS:", e)


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

@app.post("/generate/brain")
async def generate_brain_route(payload: dict):
    return await generate_campaign_brain(payload)

