FROM node:18  # o runpod/pytorch:... si necesitas CUDA/GPU para video gen

WORKDIR /app

COPY package*.json ./
RUN npm install --production

COPY . .

# RunPod Serverless ejecuta este CMD automáticamente
CMD ["node", "handler.js"]
