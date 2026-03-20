import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";

import generateRoute from "./routes/generate.js";
import runpodRoutes from "./routes/runpodRoutes.js";
import statsRoute from "./routes/stats.js";

dotenv.config();

const app = express();

// Necesario para rutas absolutas
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// ⭐ CORS CORREGIDO PARA SHOPIFY Y FRONTEND REAL
app.use(
  cors({
    origin: [
      "https://admin.shopify.com",
      "https://greenpowertech.store",
      process.env.FRONTEND_URL
    ],
    methods: ["GET", "POST", "PUT", "DELETE"],
    credentials: true,
  })
);

app.use(express.json());

// ⭐ ENDPOINT RAÍZ — SOLO API, SIN FRONTEND
app.get("/", (req, res) => {
  res.json({
    status: "ok",
    message: "Backend funcionando correctamente",
    backend: process.env.BACKEND_URL,
    frontend: process.env.FRONTEND_URL
  });
});

// ⭐ RUTAS API
app.use("/api/generate", generateRoute);
app.use("/api/runpod", runpodRoutes);
app.use("/api

