from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from workers.svd_xt import generate_svd_xt
from workers.llm_brain import generate_campaign_brain
from groq import Groq
import os
import boto3
from botocore.client import Config

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
# CONFIGURACIÓN CLOUDFLARE R2
# ---------------------------------------------------------
R2_ACCESS_KEY_ID = os.getenv("R2_ACCESS_KEY_ID")
R2_SECRET_ACCESS_KEY = os.getenv("R2_SECRET_ACCESS_KEY")
R2_BUCKET = os.getenv("R2_BUCKET")
R2_ENDPOINT = os.getenv("R2_ENDPOINT")

s3_client = boto3.client(
    "s3",
    endpoint_url=R2_ENDPOINT,
    aws_access_key_id=R2_ACCESS_KEY_ID,
    aws_secret_access_key=R2_SECRET_ACCESS_KEY,
    config=Config(signature_version="s3v4"),
    region_name="auto"
)

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
# ENDPOINT NUEVO: RECIBIR VIDEO DESDE KAGGLE Y SUBIRLO A R2
# ---------------------------------------------------------
@app.post("/kaggle-engine")
async def receive_kaggle_video(file: UploadFile = File(...)):
    # Guardar temporalmente
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    # Subir a Cloudflare R2
    try:
        s3_client.upload_file(
            temp_path,
            R2_BUCKET,
            file.filename,
            ExtraArgs={"ContentType": "video/mp4"}
        )
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error subiendo a R2: {str(e)}"
        }

    # URL público del video
    public_url = f"{R2_ENDPOINT}/{R2_BUCKET}/{file.filename}"

    return {
        "status": "ok",
        "filename": file.filename,
        "r2_url": public_url,
        "message": "Video recibido y subido correctamente a Cloudflare R2"
    }
