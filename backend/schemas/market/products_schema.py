from fastapi import File, UploadFile
from pydantic import BaseModel
from typing import Optional


class ProductAdd(BaseModel):
    name: str
    description: str
    tags: str
    price: int
    brand: int
    category: int


class ProductGet(ProductAdd):
    id: int


class ProductEdit(BaseModel):
    name: Optional[str]
    description: Optional[str]
    tags: Optional[str]
    price: Optional[int]
    brand: Optional[int]
    category: Optional[int]
    photo: Optional[str]
