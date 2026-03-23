import runpod from 'runpod-sdk';

export const handler = async (job) => {
  console.log('Job recibido en RunPod Serverless:', job.input);

  const input = job.input || {};

  if (!input.prompt || !input.duration || !input.resolution) {
    throw new Error('Faltan prompt, duration o resolution');
  }

  console.log('Iniciando generación simulada para:', input.prompt);
  await new Promise(resolve => setTimeout(resolve, 5000));

  return {
    output: {
      videoUrl: `https://example.com/simulated-video-${Date.now()}.mp4`,
      prompt: input.prompt,
      duration: input.duration,
      resolution: input.resolution,
      status: 'completed',
      message: 'Video generado (simulado)'
    }
  };
};

// ESTA LÍNEA ES OBLIGATORIA EN RUNPOD SERVERLESS
runpod.serverless.start({ handler });
