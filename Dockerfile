FROM runpod/pytorch:2.4.0-py3.11-cuda12.1-ubuntu22.04  # Usa esta si necesitas GPU/CUDA; si no, cambia a node:20

WORKDIR /app

COPY package*.json ./

RUN npm install --production

COPY . .

# RunPod llama automáticamente a handler.handler
CMD ["node", "handler.js"]
