import React from 'react'
import Carousel from 'react-bootstrap/Carousel';
import 'bootstrap/dist/css/bootstrap.min.css';
import string from "./assets/string.jpg";
import string12 from "./assets/string12.jpeg";

export const CarouselComponent = () => {
  return (
<Carousel data-bs-theme="dark" style={{height: "500px" }} className="mx-auto rounded">
      <Carousel.Item>
        <img
          className="d-block w-100"
          src={string12}
          alt="First slide"
          style={{ height: "600px", objectFit: "cover" }}
        />
        <Carousel.Caption>
          <h5>First slide label</h5>
          <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img
          className="d-block w-100"
          src={string}
          alt="Second slide"
          style={{ height: "600px", objectFit: "cover" }}
        />
        <Carousel.Caption>
          <h5>Second slide label</h5>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img
          className="d-block w-100"
          src={string12}
          alt="Third slide"
          style={{ height: "600px",  objectFit: "cover" }}
        />
        <Carousel.Caption>
          <h5>Third slide label</h5>
          <p>
            Praesent commodo cursus magna, vel scelerisque nisl consectetur.
          </p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  )
}
