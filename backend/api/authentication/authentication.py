from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from core import settings, db_helper
from schemas.authentication.jwt_token import TokenSchema
from backends.authentication.user import validate_user
from backends.authentication.schemas import UserValidate
from core.utils import encode

router = APIRouter(tags=["Authorization"])

@router.post("/login", response_model=TokenSchema)
async def login(
    credentials: dict = Depends(validate_user)):
    payload = {
        "user_id": credentials.id,
        "username": credentials.username
    }
    token = encode(payload=payload)
    return TokenSchema(access_token=token)