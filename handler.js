// handler.js - RunPod Serverless (Node.js)

// Importa tu función real de generación de video (ajusta path)
import { generateVideo } from './controllers/generateController.js'; // o './routes/generate.js' si exportas desde allí

export const handler = async (job) => {
  console.log('Serverless job input:', job.input);

  const input = job.input || {};

  if (!input.prompt || !input.duration || !input.resolution) {
    throw new Error('Missing prompt, duration or resolution');
  }

  try {
    // Ejecuta tu lógica (async, GPU si aplica, sin listen/port)
    const result = await generateVideo(input); // { videoUrl, metadata, ... }

    return result; // RunPod lo envía como output
  } catch (err) {
    console.error('Job error:', err);
    throw err;
  }
};
