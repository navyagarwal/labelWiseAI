import React, { useEffect, useState } from "react";
import axios from "axios";
import Card from "../components/card"; // Import the Card component
import { SimpleGrid } from "@chakra-ui/react";
const Home = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://localhost:4000/api/allProducts"
        );
        setData(response.data);
      } catch (error) {
        console.error("Error in fetching data", error);
      }
    };

    fetchData();
  }, []);

  console.log(data);

  return (
    <div className="container">
      <h1>Product Catalog</h1>

      {/* <pre>{JSON.stringify(data, null, 2)}</pre> */}
      <div className="card-container">
        <SimpleGrid
          spacing={4}
          templateColumns="repeat(auto-fill, minmax(200px, 1fr))"
        >
          {data.map((item) => (
            <Card
              key={item.id}
              title={item.name}
              healthLabels={item["analysis-labels"]}
              imageUrl={item["image-url"]}
            />
          ))}
        </SimpleGrid>
      </div>
    </div>
  );
};

export default Home;
