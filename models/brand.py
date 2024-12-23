from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from models import Basemodel


class Brand(Basemodel):
    __tablename__ = "brands"

    name = mapped_column(String(length=150), nullable=False)