from pydantic import BaseModel


class Number(BaseModel):
    number: str

class VerifyCode(Number):
    code: int 