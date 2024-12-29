import random
from fastapi import APIRouter, HTTPException, status, responses
from pydantic import BaseModel
from authenticator.api.v1.send_code import send_code
from core import db_redis


router = APIRouter(prefix="/redis/test", tags=["test verufication with redis"])

class Number(BaseModel):
    number: str

class VerifyCode(Number):
    code: int 


@router.post("/")
async def send_coder(data: Number):
    if not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad request")
    code = random.randint(100000, 999999)
    id = random.randint(1000000, 9999999)
    db_redis.setex(f"verification:{id}", 900, code) # 15 minutes
    return await send_code(user_id=id, data=code)

