import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import generateRoute from "./routes/generate.js";

dotenv.config();

const app = express();

app.use(cors());
app.use(express.json());

app.use("/api/generate", generateRoute);

const PORT = process.env.PORT || 4000;

app.listen(4000, () => {
  console.log("Backend running on port 4000");
});


