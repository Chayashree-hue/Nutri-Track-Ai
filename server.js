const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.send("NutriTrack backend running");
});

app.post("/login", (req, res) => {

  const { username, password } = req.body;

  res.json({
    token: "nutri_token",
    username
  });

});

app.post("/register", (req, res) => {

  res.json({
    success: true
  });

});

app.get("/recipes/:query", async (req, res) => {

  const query = req.params.query;

  try {

    const response = await fetch(
      `https://api.spoonacular.com/recipes/complexSearch?query=${query}&number=10&addRecipeNutrition=true&apiKey=8cb3003ec59e4f09885e5857a0800c18`
    );

    const data = await response.json();

    res.json(data);

  } catch (err) {

    res.json({
      results: []
    });

  }

});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log("Server running");
});