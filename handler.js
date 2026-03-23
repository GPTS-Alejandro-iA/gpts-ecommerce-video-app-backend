// handler.js - Versión debug para Render

export const handler = async (job) => {
  console.log('Serverless job input:', job.input);

  const input = job.input || {};

  if (!input.prompt || !input.duration || !input.resolution) {
    throw new Error('Missing prompt, duration or resolution');
  }

  try {
    // Placeholder: simula tu lógica de video (reemplaza con la real cuando exportes correctamente)
    console.log('Simulando generación de video...');
    await new Promise(resolve => setTimeout(resolve, 3000)); // 3s delay fake

    return {
      output: {
        videoUrl: 'https://example.com/simulated-video.mp4',
        duration: input.duration,
        resolution: input.resolution,
        status: 'completed'
      }
    };
  } catch (err) {
    console.error('Job error:', err.message);
    throw err;
  }
};

// Si usas runpod-sdk (opcional en Render, pero para compat RunPod)
// import runpod from 'runpod-sdk';
// runpod.serverless.start({ handler });
