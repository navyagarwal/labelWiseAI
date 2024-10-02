require("dotenv").config();
const express = require("express");
const cors = require("cors");

const productRoutes = require("./routes/product");

// express app
const app = express();

// middleware
app.use(express.json());
app.use(cors());

app.use("/api", productRoutes);

app.listen(4000, () => {
  console.log("Server is running on port 3000");
});
