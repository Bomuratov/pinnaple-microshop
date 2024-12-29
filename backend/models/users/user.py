import re
import bcrypt
from sqlalchemy.orm import mapped_column, validates
from sqlalchemy import String, Boolean
from models import Basemodel
from core.utils import hashing_password
from core import db_helper

class UserModel(Basemodel):
    __tablename__="users"

    username = mapped_column(String(length=150), nullable=False)
    email = mapped_column(String, nullable=False)
    phone = mapped_column(String, nullable=False)
    password = mapped_column(String, nullable=False)
    name = mapped_column(String(length=150), nullable=False)
    surname = mapped_column(String(length=150), nullable=False)
    is_active = mapped_column(Boolean, default=False)
    is_superuser = mapped_column(Boolean, default=False)
    is_staff = mapped_column(Boolean, default=False)
    is_manager = mapped_column(Boolean, default=False)
    
    
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Хеширует пароль с использованием bcrypt.
        """
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

    @validates("password")
    def validate_password(self, key, value):
        if len(value) < 8:
            raise ValueError("Пароль должень быть минимум восьми символов")
        if not re.match(r"^(?=.*[A-Z])(?=.*\d)(?=.*[-_()+=!]).+$", value):
            raise ValueError("Пароль должен содержать минимун одна буква верхного регистра, минимум одна цифра и минимум один из этих символов - _ ( ) + = !")
        return self.hash_password(value)


    @validates("username")
    def validate_username(self, key, value):
        if not re.match(r"^[a-z0-9-]+$", value):
            raise ValueError("The username can only contain lowercase letters, numbers, and symbols.")
        return value
    
    
    @validates("email")
    def validate_email(self, key, value):
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
            raise ValueError("Похоже вы указали неправильный email адрес проверьте поля email и попробуйте заново")
        return value
    

    @validates("phone")
    def validate_phone(self, key, value):
        if not re.match(r"^\+998[0-9]{9}$", value):
            raise ValueError("Неправильный формат номера (пример: +998ZZZXXYYZZ)")
        return value
