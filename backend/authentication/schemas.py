from pydantic import BaseModel

class UserValidate(BaseModel):
    username: str
    password: str