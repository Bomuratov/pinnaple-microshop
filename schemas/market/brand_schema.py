from pydantic import BaseModel


class BrandAddOrEdit(BaseModel):
    name: str

class BrandGet(BrandAddOrEdit):
    id: int
