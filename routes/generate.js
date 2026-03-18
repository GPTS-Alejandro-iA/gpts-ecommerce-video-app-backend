import express from "express";
import upload from "../middleware/upload.js";
import { generateVideoController } from "../controllers/generateController.js";

const router = express.Router();

router.post("/", upload.single("file"), generateVideoController);

export default router;

