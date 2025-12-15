import React, { useEffect, useState } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import axios from "axios";

const FormProduct = () => {
  const [formData, setFormData] = useState({
    name: "",
    description: "",
    price: "",
    category: "",
    restaurant: "",
    restaurantName: "",
    photo: "",
    isActive: false,
  });

  const [categories, setCategories] = useState([]);
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    getRestaurants();
  }, []);

  useEffect(() => {
    if (formData.restaurantName) {
      getCategories(formData.restaurantName);
    }
  }, [formData.restaurantName]);

  const getCategories = async (restaurantName) => {
    try {
      const response = await axios.get(
        `http://localhost:8000/api/v1/category?restaurant__name=${restaurantName}`
      );
      setCategories(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const getRestaurants = async () => {


    try {
      const response = await axios.get(
        "http://localhost:8000/api/v1/restaurant/"
      );
      setRestaurants(response.data);
    } catch (error) {
      console.error(error);
    }
  };


  const handleChange = (e) => {
    const { name, value, type, checked, files } = e.target;




    if (name === "restaurant" && name !== "photo") {
      const selectedRestaurant = restaurants.find(
        (rest) => rest.id.toString() === value
      );
      setFormData((prevData) => ({
        ...prevData,
        restaurant: value,
        restaurantName: selectedRestaurant ? selectedRestaurant.name : "", // 👈 Запоминаем название ресторана
      }));


    } else {
      setFormData((prevData) => ({
        ...prevData,
        [name]: type === "checkbox" ? checked : value,
      }));
    }
     
    if (name === "photo" && files) {
        setFormData((prevData) => ({
          ...prevData,
          [name]: files[0],
        }));
      }

  };

  console.log(formData.photo)  

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const formDataPhoto = new FormData();
    formDataPhoto.append("photo", formData.photo);

    try {
      await axios
        .post("http://localhost:8000/api/v1/menu/", formData)
        .then((response) => updateThumb(response.data.data.id, formDataPhoto));


    } catch (error) {
      console.error("Error adding product:", error);
      alert("Failed to add product.");
    }
  };

  const updateThumb = async (id, formDataPhoto) => {
    await axios.put(
      `http://localhost:8000/api/v1/menu/thumb/${id}`,formDataPhoto
    );
  };

  

  return (
    <div className="container w-50 my-5">
      <Form onSubmit={handleSubmit}>
        <Form.Group className="mb-3" controlId="formBasicName">
          <Form.Label>Name</Form.Label>
          <Form.Control
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="Enter product name"
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicDescription">
          <Form.Label>Description</Form.Label>
          <Form.Control
            type="text"
            name="description"
            value={formData.description}
            onChange={handleChange}
            placeholder="Enter product description"
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPrice">
          <Form.Label>Price</Form.Label>
          <Form.Control
            type="number"
            name="price"
            value={formData.price}
            onChange={handleChange}
            placeholder="Enter product price"
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicRestaurant">
          <Form.Label>Restaurant</Form.Label>
          <Form.Select
            name="restaurant"
            value={formData.restaurant}
            onChange={handleChange}
          >
            <option value="">Select restaurant</option>
            {restaurants.map((rest) => (
              <option key={rest.id} value={rest.id}>
                {rest.name}
              </option>
            ))}
          </Form.Select>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicCategory">
          <Form.Label>Category</Form.Label>
          <Form.Select
            name="category"
            value={formData.category}
            onChange={handleChange}
          >
            <option value="">Select category</option>
            {categories.map((cat) => (
              <option key={cat.id} value={cat.id}>
                {cat.name}
              </option>
            ))}
          </Form.Select>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicCategory">
          <Form.Label>Image</Form.Label>
          <Form.Control type="file" onChange={handleChange} name="photo" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicCheckbox">
          <Form.Check
            type="checkbox"
            name="isActive"
            checked={formData.isActive}
            onChange={handleChange}
            label="Product is active"
          />
        </Form.Group>

        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </div>
  );
};

export default FormProduct;
