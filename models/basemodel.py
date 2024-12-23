from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Integer


class Basemodel(DeclarativeBase):
    __abstract__=True

    id = mapped_column(Integer, primary_key=True)