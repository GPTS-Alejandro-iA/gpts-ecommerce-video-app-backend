import express from "express";
import { generarImagen, generarVideoDesdeImagen } from "../controllers/runpodController.js";

const router = express.Router();

router.post("/generar", async (req, res) => {
  try {
    const { prompt } = req.body;

    // 1. Generar imagen
    const imagen = await generarImagen(prompt);

    // 2. Generar video usando la imagen generada
    const video = await generarVideoDesdeImagen(imagen.output, prompt);

    res.json({
      ok: true,
      imagen: imagen.output,
      video: video.output
    });

  } catch (error) {
    console.error(error);
    res.status(500).json({ ok: false, error: error.message });
  }
});

export default router;

