import express from "express";
import cors from "cors";
import dotenv from "dotenv";

// Rutas
import generateRoute from "./routes/generate.js";
import runpodRoutes from "./routes/runpodRoutes.js";

dotenv.config();

const app = express();

app.use(cors());
app.use(express.json());

// Ruta existente
app.use("/api/generate", generateRoute);

// Nueva ruta RunPod
app.use("/api/runpod", runpodRoutes);

const PORT = process.env.PORT || 4000;

app.listen(PORT, () => {
  console.log(`Backend running on port ${PORT}`);
});
