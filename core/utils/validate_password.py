import bcrypt


def validate_password(password: str, hashed_password: bytes)-> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password,)