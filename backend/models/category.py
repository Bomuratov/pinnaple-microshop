from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from models import Basemodel


class Category(Basemodel):
    __tablename__ = "categorys"

    name = mapped_column(String(length=150), nullable=False)
