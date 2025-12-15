import React from "react";
import aurora from './assets/aurora.png'
import user from "./assets/user.jpg"
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Image from 'react-bootstrap/Image'
import styles from './Header.module.scss';


export const Header = () => {
  return (
      <div className={styles.container}>
        <div className={styles.navbar}>
          <div className={styles.logo}>
            <a href="https://react.dev" target="_blank">
              <img src={aurora} className="logo react" alt="React logo" />
            </a>
          </div>
          <div className="search d-flex">            
            <Form.Control
              type="text"
              placeholder="Search"
              className=" mr-sm-2"
            />
            <div className="ms-2"><Button variant="outline-dark" type="submit">Submit</Button></div>
            
            </div>
          <div className={styles.user}>
            <div className={styles.user_info}>John Doe</div>
            <div className={styles.user_image}><Image src={user} roundedCircle /></div>
            </div>
        </div>
      </div>
  );
};
