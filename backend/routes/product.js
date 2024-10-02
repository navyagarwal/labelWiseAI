const express = require("express");
const router = express.Router();
const { getAllProducts } = require("../controllers/product");

// GET all products, currently the catalog is read only
router.get("/allProducts", getAllProducts);

module.exports = router;
