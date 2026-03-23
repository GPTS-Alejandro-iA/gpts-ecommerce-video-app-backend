// handler.js - Para RunPod Serverless (compatible con tu backend)

import { generateVideo } from './controllers/generateController.js'; // ajusta según tu controller real
// o importa lo que necesites para /api/generate

export const handler = async (event) => {
  console.log('Job recibido:', event.input);

  try {
    const input = event.input; // { prompt, duration, resolution, ... }

    if (!input.prompt || !input.duration) {
      throw new Error('Faltan parámetros requeridos');
    }

    // Llama a tu lógica real de generación de video
    const result = await generateVideo(input); // adapta al nombre de tu función

    return {
      output: result, // { videoUrl, jobId, status, ... }
      status: 'COMPLETED'
    };
  } catch (error) {
    console.error('Error en handler:', error);
    return {
      error: error.message,
      status: 'FAILED'
    };
  }
};
