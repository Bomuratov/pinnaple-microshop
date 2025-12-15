import { useState } from 'react'
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Header } from './header'
import { CarouselComponent } from './CarouselComponent.jsx'
import Product from './Product.jsx'
import FormProduct from './FormProduct.jsx';
import Category from './Category.jsx';




function App() {

  const [from, setForm] = useState(false)

  const handlerForm = () => {
    setForm(!from)
  }

  return (
    <>
    <Header/>
    <button className='btn btn-outline-primary ms-2 mt-2' onClick={handlerForm} > Add Product</button>
    {from && <FormProduct/>}
    {/* <Product/> */}
    <Category/>

    </>
  )
}

export default App
