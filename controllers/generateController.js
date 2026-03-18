export async function generateVideoController(req, res) {
  try {
    const prompt = req.body.prompt;
    const file = req.file;

    console.log("Prompt recibido:", prompt);
    console.log("Archivo recibido:", file?.originalname);

    // Aquí luego conectamos con tu motor de video (OpenAI, Luma, Runway, etc.)
    // Por ahora devolvemos un video de prueba

    return res.json({
      videoUrl: "https://samplelib.com/lib/preview/mp4/sample-5s.mp4"
    });

  } catch (error) {
    console.error("Error generating video:", error);
    res.status(500).json({ error: "Error generating video" });
  }
}

