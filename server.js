import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";

import generateRoute from "./routes/generate.js";
import runpodRoutes from "./routes/runpodRoutes.js";

dotenv.config();

const app = express();

// Necesario para rutas absolutas
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.use(cors());
app.use(express.json());

// Servir dashboard desde /public
app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public/index.html"));
});

// API
app.use("/api/generate", generateRoute);
app.use("/api/runpod", runpodRoutes);

const PORT = process.env.PORT || 4000;

app.listen(PORT, () => {
  console.log(`Backend running on port ${PORT}`);
});
