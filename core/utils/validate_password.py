import bcrypt


def validate_password(password: str, hashed_password: bytes)-> bool:
    return bcrypt.checkpw(password=password.encode("utf-8"), hashed_password=hashed_password.encode("utf-8"),)