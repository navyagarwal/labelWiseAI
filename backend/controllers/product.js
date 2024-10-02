require("dotenv").config({ path: "../.env" });
const { db } = require("../firestore");

const getAllProducts = async (req, res) => {
  try {
    const productsRef = db.collection("Products");
    const snapshot = await productsRef.get();

    if (snapshot.empty) {
      return res.status(404).json({ message: "No products found" });
    }

    const products = snapshot.docs.map((doc) => ({
      id: doc.id,
      ...doc.data(),
    }));

    return res.status(200).json(products);
  } catch (error) {
    console.error("Error in fetching products:", error);
    return res.status(500).json({ message: "Error in fetching products" });
  }
};

module.exports = { getAllProducts };
