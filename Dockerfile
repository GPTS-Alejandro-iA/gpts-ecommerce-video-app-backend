FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install --production

COPY . .

# Ejecuta el handler (RunPod Serverless lo llama automáticamente)
CMD ["node", "handler.js"]
