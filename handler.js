import runpod from "runpod";

export const handler = async (event) => {
  return {
    status: "success",
    message: "Handler funcionando.",
    input: event
  };
};

runpod.serverless.start({
  handler
});

