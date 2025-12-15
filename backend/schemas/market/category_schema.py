from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str


class CategoryGET(CategoryCreate):
    id: int
