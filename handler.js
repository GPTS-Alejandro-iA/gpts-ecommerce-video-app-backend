"use strict";

const runpod = require("runpod-sdk");

/**
 * Runpod Serverless handler.
 * job format:
 * {
 *   "id": "...",
 *   "input": { "prompt": "texto" },
 *   ...
 * }
 */
function handler(job) {
  const input = job && job.input ? job.input : {};
  const prompt = input.prompt;

  if (typeof prompt !== "string") {
    return {
      status: "error",
      error: "Invalid input: expected input.prompt to be a string"
    };
  }

  return {
    status: "ok",
    echo: prompt
  };
}

// Start the serverless worker loop
runpod.serverless.start({ handler });
