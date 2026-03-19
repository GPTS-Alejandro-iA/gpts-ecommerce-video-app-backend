import express from "express";
import { generarImagen, generarVideoDesdeImagen } from "../controllers/runpodController.js";

const router = express.Router();

// GET para validar desde navegador y Shopify
router.get("/generar", (req, res) => {
  res.send("RunPod API funcionando correctamente.");
});

// POST real para generar imagen + video
router.post("/generar", async (req, res) => {
  try {
    const { prompt } = req.body;

    if (!prompt) {
      return res.status(400).json({ ok: false, error: "Falta el prompt." });
    }

    // 1. Generar imagen
    const imagen = await generarImagen(prompt);

    // Validación defensiva
    if (!imagen || !imagen.output) {
      return res.status(500).json({ ok: false, error: "Error generando imagen." });
    }

    // 2. Generar video usando la imagen generada
    const video = await generarVideoDesdeImagen(imagen.output, prompt);

    if (!video || !video.output) {
      return res.status(500).json({ ok: false, error: "Error generando video." });
    }

    res.json({
      ok: true,
      imagen: imagen.output,
      video: video.output
    });

  } catch (error) {
    console.error("Error en /api/runpod/generar:", error);
    res.status(500).json({ ok: false, error: error.message });
  }
});

export default router;


