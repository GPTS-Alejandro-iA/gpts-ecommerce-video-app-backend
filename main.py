from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from workers.svd_xt import generate_svd_xt
from workers.llm_brain import generate_campaign_brain
from groq import Groq
import os

# ---------------------------------------------------------
# Inicializar FastAPI
# ---------------------------------------------------------
app = FastAPI()

# ---------------------------------------------------------
# MODELOS GROQ (TEMPORAL)
# ---------------------------------------------------------
try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    models = client.models.list()
    print(">>> MODELOS DISPONIBLES EN GROQ <<<")
    for m in models.data:
        print(" -", m.id)
    print(">>> FIN DE LISTA <<<")
except Exception as e:
    print(">>> ERROR LISTANDO MODELOS:", e)

# ---------------------------------------------------------
# MODELO PARA PETICIONES DE TEXTO
# ---------------------------------------------------------
class VideoRequest(BaseModel):
    prompt: str

# ---------------------------------------------------------
# ENDPOINT PRINCIPAL
# ---------------------------------------------------------
@app.get("/")
def root():
    return {"status": "Backend running"}

# ---------------------------------------------------------
# ENDPOINT DE PRUEBA DE VIDEO
# ---------------------------------------------------------
@app.post("/generate-video")
def generate_video(request: VideoRequest):
    return {
        "message": "Video generado correctamente",
        "prompt_recibido": request.prompt
    }

# ---------------------------------------------------------
# ENDPOINT REAL PARA SVD-XT
# ---------------------------------------------------------
@app.post("/generate/svd_xt")
async def generate_svd_xt_route(request: VideoRequest):
    return await generate_svd_xt(request)

# ---------------------------------------------------------
# ENDPOINT PARA GENERAR CAMPAÑA (LLM BRAIN)
# ---------------------------------------------------------
@app.post("/generate/brain")
async def generate_brain_route(payload: dict):
    return await generate_campaign_brain(payload)

# ---------------------------------------------------------
# ENDPOINT NUEVO: RECIBIR VIDEO DESDE KAGGLE
# ---------------------------------------------------------
@app.post("/kaggle-engine")
async def receive_kaggle_video(file: UploadFile = File(...)):
    # Guardar el archivo temporalmente
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    return {
        "status": "ok",
        "filename": file.filename,
        "message": "Video recibido correctamente"
    }



