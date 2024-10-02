// CardComponent.js
import React from "react";
import { Box, Heading, Text, Badge, Button } from "@chakra-ui/react";
import { Card, CardBody, CardHeader, CardFooter } from "@chakra-ui/react";
const ProductCard = ({ title, healthLabels, imageUrl }) => {
  return (
    // <Box
    //   borderWidth="1px"
    //   bgColor="#c8f5f3"
    //   borderRadius="lg"
    //   overflow="hidden"
    //   width="200px"
    //   m="2"
    // >
    //   {/* <Image
    //     src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Ffood&psig=AOvVaw1HVPQeemAX27us0bq2MWXt&ust=1727976761792000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCODb3pqd8IgDFQAAAAAdAAAAABAQ"
    //     alt={title}
    //   /> */}
    //   <Box p="10">
    //     <Text fontWeight="bold" fontSize="xll">
    //       {title}
    //     </Text>
    //     {healthLabels.map((label, index) => (
    //       <Badge key={index} colorScheme="teal" mr="1">
    //         {label}
    //       </Badge>
    //     ))}
    //   </Box>
    // </Box>

    <Card bgColor="#c8f5f3">
      <CardHeader>
        <Heading size="md"> {title}</Heading>
      </CardHeader>
      <CardBody>
        <Box p="10">
          <Text fontWeight="bold" fontSize="xll"></Text>
          {healthLabels.map((label, index) => (
            <Badge key={index} colorScheme="teal" mr="10">
              {label}
            </Badge>
          ))}
        </Box>
      </CardBody>
      {/* <CardFooter>
        <Button>View more</Button>
      </CardFooter> */}
    </Card>
  );
};

export default ProductCard;
