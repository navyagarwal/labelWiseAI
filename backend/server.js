require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

// express app
const app = express();

// middleware
app.use(express.json());
app.use(cors());

const connectToDB = async () => {
  mongoose.connect(process.env.MONGO_URI).catch((err) => {
    console.log(err);
  });
};

// connect to db
const startServer = async () => {
  mongoose
    .connect(process.env.MONGO_URI)
    .then(() => {
      // listen for requests
      app.listen(process.env.PORT, () => {
        console.log("hey! connected to db and server started at port");
      });
    })
    .catch((err) => {
      console.log(err);
    });
};

module.exports = connectToDB;
