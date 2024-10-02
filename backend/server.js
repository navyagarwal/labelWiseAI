require("dotenv").config();
const express = require("express");
const cors = require("cors");

// express app
const app = express();

// middleware
app.use(express.json());
app.use(cors());

// Initialize Firebase Admin SDK
var admin = require("firebase-admin");

const serviceAccount = {
  type: process.env.FIREBASE_TYPE,
  project_id: process.env.FIREBASE_PROJECT_ID,
  private_key_id: process.env.FIREBASE_PRIVATE_KEY_ID,
  private_key: process.env.FIREBASE_PRIVATE_KEY.replace(/\\n/g, "\n"), // Ensure newlines are correct
  client_email: process.env.FIREBASE_CLIENT_EMAIL,
  client_id: process.env.FIREBASE_CLIENT_ID,
  auth_uri: process.env.FIREBASE_AUTH_URI,
  token_uri: process.env.FIREBASE_TOKEN_URI,
  auth_provider_x509_cert_url: process.env.FIREBASE_AUTH_PROVIDER_X509_CERT_URL,
  client_x509_cert_url: process.env.FIREBASE_CLIENT_X509_CERT_URL,
  universe_domain: process.env.FIREBASE_UNIVERSE_DOMAIN,
};

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

// Firestore instance using Firebase Admin SDK
const db = admin.firestore();

// Example function to store data scraped into Firestore
// async function storeScrapedData(data) {
// }

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});

module.exports = { db };
