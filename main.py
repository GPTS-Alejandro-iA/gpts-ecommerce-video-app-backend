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




