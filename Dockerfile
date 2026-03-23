FROM node:18-slim

WORKDIR /app

# Copiamos manifests primero para aprovechar cache de Docker
COPY package.json package-lock.json* ./

# Instala dependencias de producción
# (npm ci si hay lockfile; si no, npm install)
RUN if [ -f package-lock.json ]; then npm ci --omit=dev; else npm install --omit=dev; fi

# Copia el código del worker
COPY handler.js ./

# Arranca el worker
CMD ["node", "handler.js"]
