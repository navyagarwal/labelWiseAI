/*
  - currently scrapes a specific number of top products under particular category
  - can change parameters to set the number of products
  - scrapes all images for a product

*/

require("dotenv").config({ path: "../.env" });
const puppeteer = require("puppeteer");
const { db } = require("../firestore");

async function getTopSubcategories(page, categoryUrl, numberOfCategories) {
  await page.goto(categoryUrl, {
    waitUntil: "networkidle0",
  });

  await page.waitForSelector("nav.category-list a");

  const navbarLinks = await page.$$eval(
    "nav.category-list a",
    (anchorTags, numberOfCategories) => {
      return anchorTags
        .slice(0, numberOfCategories)
        .map((anchor) => anchor.href);
    },
    numberOfCategories
  );

  return navbarLinks;
}

async function getTopProductLinks(page, subcategoryUrl, numberOfProducts) {
  page.goto(subcategoryUrl, {
    waitUntil: "networkidle0",
  });

  await page.waitForSelector('a[data-test-id="plp-product"]');

  const productLinks = await page.$$eval(
    'a[data-test-id="plp-product"]',
    (anchorTags, numberOfProducts) => {
      return anchorTags.slice(0, numberOfProducts).map((anchor) => anchor.href);
    },
    numberOfProducts
  );

  return productLinks;
}

async function getImagesOfProduct(page, productLink) {
  page.goto(productLink, {
    waitUntil: "networkidle0",
  });

  await page.waitForSelector("section.carousel-content img");

  const imageLinks = await page.$$eval(
    "section.carousel-content img",
    (images) => {
      const updateUrl = (url) =>
        url.replace("w=120", "w=480").replace("h=120", "h=480");
      return images.map((img) => {
        let updatedSrc = updateUrl(img.src); // Call the updateUrl function to modify the src
        return updatedSrc;
      });
    }
  );

  return imageLinks;
}

async function getProductLinksInCategory(categoryUrl) {
  let browser;
  try {
    browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();

    await page.setViewport({
      width: 1920,
      height: 1080,
    });

    page.setDefaultNavigationTimeout(5 * 60 * 1000);

    const subcategories = await getTopSubcategories(page, categoryUrl, 5);

    const allTopProductLinks = [];
    for (link of subcategories) {
      const productLinks = await getTopProductLinks(page, link, 5);
      allTopProductLinks.push(...productLinks);
    }
    console.log(allTopProductLinks.length);

    const newProducts = await filterNewLinks(allTopProductLinks);
    console.log(newProducts.length);

    // topNewProducts = await filterNewLinks(allTopProductLinks)

    const firstProduct = newProducts[0];
    const imagesLinks = await getImagesOfProduct(page, firstProduct);

    console.log(imagesLinks);

    await browser?.close();
  } catch (error) {
    console.log(error);
    await browser?.close();
  }
}

// getProductLinksInCategory("https://blinkit.com/cn/chips-crisps/cid/1237/940");

async function addproduct() {
  try {
    const docRef = await db.collection("Products").add({
      name: "name",
      "analysis-labels": "",
      image: "",
    });
    console.log("Document written with ID: ", (await docRef).id);
  } catch (error) {
    console.error("Error adding document: ", error);
  }
}

addproduct();

/*
    To be used later
*/

async function handleRestrictions() {}

async function filterNewLinks(productLinks) {
  // TODO : check new products using some unique code
  // currently it is just getting checked using links

  const newProducts = [];
  const collectionRef = db.collection("Products");

  try {
    for (var link of productLinks) {
      const querySnapshot = await collectionRef.where("link", "==", link).get();

      if (querySnapshot.empty) {
        newProducts.push(link);
      }
    }
  } catch (error) {
    console.log(error);
  }

  return newProducts;
}

// async function updateDB() {}

// module.exports = {
//   scrapeAmazonLinks,
//   getNewProducts,
//   scrapeNewProducts,
//   updateDB,
// };
