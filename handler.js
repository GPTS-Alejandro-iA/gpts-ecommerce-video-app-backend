// handler.js - RunPod Serverless entrypoint

// Importa tu lógica de generación (ajusta path/nombre exacto)
import { generateVideo } from './controllers/generateController.js'; // o './controllers/runpodController.js' si ahí está

export const handler = async (job) => {
  console.log('Serverless job input:', job.input);

  const input = job.input || {};

  // Validación (ajusta a tus params requeridos)
  if (!input.prompt || !input.duration || !input.resolution) {
    throw new Error('Missing required params: prompt, duration, resolution');
  }

  try {
    // Ejecuta tu función principal de video (debe ser async)
    const result = await generateVideo(input); // devuelve { videoUrl, metadata, ... }

    return {
      output: result,
      status: 'COMPLETED'
    };
  } catch (err) {
    console.error('Job error:', err.message);
    throw err; // RunPod marca job como FAILED
  }
};
