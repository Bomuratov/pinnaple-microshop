from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Integer
from models import Basemodel


class Product(Basemodel):
    __tablename__ = "products"

    name= mapped_column(String(length=150), nullable=False)
    description = mapped_column(String(length=550), nullable=False)
    tags = mapped_column(String(length=150), nullable=False)
    price = mapped_column(Integer, nullable=False)
    brand = mapped_column(Integer, ForeignKey("brands.id"), nullable=False)
    category = mapped_column(Integer, ForeignKey("categorys.id"), nullable=False)