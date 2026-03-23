import runpod from "runpod";

export const handler = async (event) => {
  console.log("Evento recibido:", event);

  return {
    status: "success",
    message: "Handler de RunPod funcionando correctamente.",
    input: event
  };
};

runpod.serverless.start({
  handler
});
