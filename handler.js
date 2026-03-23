module.exports = async (req, res) => {
  return res.json({
    status: "ok",
    message: "Serverless handler funcionando."
  });
};

