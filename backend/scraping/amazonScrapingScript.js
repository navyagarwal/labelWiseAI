/* Work In Progress */

require("dotenv").config({ path: "../.env" });
const mongoose = require("mongoose");
const puppeteer = require("puppeteer");
const connectToDB = require("../server");
const Product = require("../models/product");

async function scrapeAmazonLinks() {
  let browser;
  try {
    browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();

    await page.setViewport({
      width: 1080,
      height: 768,
    });

    page.setDefaultNavigationTimeout(2 * 60 * 1000);

    await page.goto("https://www.amazon.in/gp/bestsellers/grocery/", {
      waitUntil: "networkidle2",
    });

    const productLinks = [];

    //let nextPage = true;

    //while(nextPage) {

    await autoScroll(page);

    const links = await page.$$eval("#gridItemRoot a.aok-block", (anchors) =>
      anchors.map((a) => a.href).filter(Boolean)
    );
    productLinks.push(...links);

    // next page
    //const nextPageButton = await page.$()

    //}

    await browser?.close();

    // filter out new links
    const newProducts = await filterNewLinks(productLinks);
    console.log(newProducts.length);

    // scrape new links
    /* store data as

      ingredients:
      description:
      images:
      product name:
      link:
    */

    const scrapePromises = newProducts.map((link) => scrapeNewProduct(link));
    const results = await Promise.all(scrapePromises);

    console.log(results[0]);

    //scrapeNewProducts(newProducts);
  } catch (error) {
    console.log(error);
    await browser?.close();
  }
}

async function autoScroll(page) {
  await page.evaluate(async () => {
    await new Promise((resolve, reject) => {
      var totalHeightScrolled = 0;
      var scrollDistance = 100;

      var timer = setInterval(() => {
        var scrollHeight = document.body.scrollHeight;
        window.scrollBy(0, scrollDistance);
        totalHeightScrolled += scrollDistance;

        if (totalHeightScrolled >= scrollHeight) {
          clearInterval(timer);
          resolve();
        }
      }, 100);
    });
  });
}

async function filterNewLinks(productLinks) {
  // TODO : check new products using fssai licence
  // currently it is just getting checked using links

  const newProducts = [];

  try {
    await connectToDB();
    console.log("DB connected:", mongoose.connection.readyState);

    for (var link of productLinks) {
      link = link.split("/ref=")[0];
      const exists = await Product.exists({ link: link });
      if (!exists) {
        console.log(link);
        newProducts.push(link);
      }
    }

    await mongoose.disconnect();
  } catch (error) {
    console.log(error);
  }

  return newProducts;
}

scrapeAmazonLinks();

async function scrapeNewProduct(link) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  await page.goto(link, { waitUntil: "networkidle2" });

  const data = await page.evaluate(() => {
    return {
      name: "",
    };
  });

  await browser.close();
  return data;
}

// async function updateDB() {}

// module.exports = {
//   scrapeAmazonLinks,
//   getNewProducts,
//   scrapeNewProducts,
//   updateDB,
// };
