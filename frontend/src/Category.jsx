import axios from 'axios'
import React, { useEffect, useState } from 'react'

const Category = () => {

    const [data, setData] = useState(null)

    useEffect(()=>{
        getCategories()
    },[])

    const getCategories = () =>{
        axios.get("http://localhost:8000/api/v1/category/")
        .then(setData(response.data))

    }

console.log(data)
  return (
    <>
    {data?.map((product)=>{
            <h1>{product.name}</h1>
        })}

    </>
  )
  
}

export default Category