from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from core import settings, db_helper
from core.utils import decode
from models.users import UserModel


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

async def check_user(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(db_helper.session_getter)) -> dict:
    try:
        payload = decode(token=token)
        stmt = select(UserModel).where(UserModel.id == payload["user_id"])
        result = await session.execute(stmt)
        if result is None:
            raise HTTPException(status_code=404, detail="Invalid token")
        user = result.scalar_one_or_none()
        if user.is_active is False:
            raise HTTPException(status_code=403, detail="User inactive")
        return user
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")