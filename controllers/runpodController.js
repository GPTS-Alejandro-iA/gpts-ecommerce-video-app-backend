import fetch from "node-fetch";

const RUNPOD_ENDPOINT_URL = process.env.RUNPOD_ENDPOINT_URL;
const RUNPOD_API_KEY = process.env.RUNPOD_API_KEY;

// 1. Generar imagen
export async function generarImagen(prompt) {
  const response = await fetch(RUNPOD_ENDPOINT_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${RUNPOD_API_KEY}`
    },
    body: JSON.stringify({
      input: {
        type: "image",
        prompt
      }
    })
  });

  return await response.json();
}

// 2. Generar video desde imagen
export async function generarVideoDesdeImagen(imageUrl, prompt) {
  const response = await fetch(RUNPOD_ENDPOINT_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${RUNPOD_API_KEY}`
    },
    body: JSON.stringify({
      input: {
        type: "video",
        image: imageUrl,
        prompt
      }
    })
  });

  return await response.json();
}
