from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from models import Basemodel
from schemas.market.brand_schema import BrandAddOrEdit, BrandGet


class Brand(Basemodel):
    __tablename__ = "brands"

    name = mapped_column(String(length=150), nullable=False)

class Brandon(Basemodel):
    __tablename__ = "brandons"

    name = mapped_column(String(length=150), nullable=False)
    price = mapped_column(Integer, nullable=False)