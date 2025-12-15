import React, { useEffect, useState } from "react";
import axios from "axios";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import { useGetProductQuery } from "./api/products";

const Product = () => {
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    getProduct()
  }, [])

  // const { data, error, isLoading } = useGetProductQuery();
  // if (isLoading) return <p>Loading...</p>;
  // console.log(data[0].id);
  // if (error) return <p>Error: {error.message}</p>;

  const getProduct = () => {
    setLoading(true);
    axios
      .get("http://localhost:8000/api/v1/menu/")
      .then((response) => {
        setProduct(response.data);
      })
      .catch((error) => {
        console.log(error);
      })
    setLoading(false);
  }



  if (loading) return <p>Loading...</p>;

  return (
    <div className="container d-flex justify-content-center flex-wrap">
      {product?.map((product) => (
        <Card
        key={product.id}
          style={{
            width: "18rem",
            margin: "10px",
            borderRadius: "5% 5% 12px 12px",
          }}
        >
          <img
            style={{
              width: "100%",
              height: "50%",
              objectFit: "cover",
              borderRadius: "5% 5% 0 0",
            }}
            src={product.photo}
            alt=""
          />
          <Card.Body>
            <Card.Title>{product.name}</Card.Title>
            <Card.Text>{product.description}</Card.Text>
          </Card.Body>
          <ListGroup className="list-group-flush">
            <ListGroup.Item>{product.id}</ListGroup.Item>
            <ListGroup.Item>{product.category}</ListGroup.Item>
            <ListGroup.Item>{product.restaurant}</ListGroup.Item>
          </ListGroup>
          <Card.Body>
            <Card.Link className="text-decoration-none text-dark" href="#">
              Buy
            </Card.Link>
            <Card.Link href="#">Another Link</Card.Link>
          </Card.Body>
        </Card>
      ))}
    </div>
  );
};
export default Product;
