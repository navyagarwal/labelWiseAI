// models/Product.js

const mongoose = require("mongoose");

const productSchema = new mongoose.Schema({
  name: String,
  link: String, // Ensure uniqueness of product link
  fssaiLicence: String,
  analysisLabels: [String], // For example: ['Low Fat', 'High Sodium', 'Keto-Diet']
  imageUrl: String,
});

module.exports = mongoose.model("Product", productSchema);
