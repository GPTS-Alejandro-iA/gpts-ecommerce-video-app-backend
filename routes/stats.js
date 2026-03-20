import express from "express";
const router = express.Router();

router.get("/", async (req, res) => {
  try {
    const data = {
      kpis: {
        videos: 27,
        projects: 8,
        scenes: 142,
        published: 19,
      },
      week: {
        labels: ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
        values: [3, 5, 2, 8, 6, 4, 7],
      },
      projects: {
        completed: 12,
        active: 7,
        pending: 4,
      },
    };

    res.json(data);
  } catch (error) {
    console.error("Error en /api/stats:", error);
    res.status(500).json({ error: "Error interno del servidor" });
  }
});

export default router;

