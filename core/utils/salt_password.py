import bcrypt

def hashing_password(password: str) -> str:
    salt = bcrypt.gensalt()
    password_bytes: bytes = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    print(hashed_password)
    print(type(hashed_password))
    print(hashed_password.decode("utf-8"))
    print(type(hashed_password))
    return hashed_password.decode("utf-8")