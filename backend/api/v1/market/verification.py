import redis
import random
from fastapi import APIRouter, HTTPException, status, responses
from pydantic import BaseModel



db_redis = redis.Redis(host="localhost", port=6379, db=0)

router = APIRouter(prefix="/redis/test", tags=["test verufication with redis"])

class Number(BaseModel):
    number: str

class VerifyCode(Number):
    code: int 

user_id = {
    "id": 5092708098
}

@router.post("/")
async def send_coder(data: Number):
    if not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad request")
    code = random.randint(100000, 999999)
    db_redis.setex(f"verification:{data.number}", 900, code) # 60 seconds
    return {
        "status": status.HTTP_200_OK,
        "detail": "Verification code succesfuly send"
    }

    # stored_code = db_redis.get(f"verification:{data.number}")
