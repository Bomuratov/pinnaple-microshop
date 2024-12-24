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
    

class CheckUser:
    def __init__(self):
        pass

    async def check_user(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(db_helper.session_getter)) -> dict:
        try:
            payload = decode(token=token)
            stmt = select(UserModel).where(UserModel.id == payload["user_id"])
            result = await session.execute(stmt)
            if result is None:
                raise HTTPException(status_code=401, detail="Not found")
            user = result.scalar_one_or_none()
            if user.is_active is False:
                raise HTTPException(status_code=401, detail="Inactive")
            return user
        except jwt.PyJWTError:
            raise HTTPException(status_code=401, detail="Invalid Token")
    
    async def check_is_staff(user: UserModel = Depends(check_user)):
        if not user.is_staff:
            raise HTTPException(status_code=403, detail="No staff")
        return user

    async def check_is_manager(user: UserModel = Depends(check_user)):
        if not user.is_manager:
            raise HTTPException(status_code=403, detail="No manager")
        return user

    async def check_is_superuser(user: UserModel = Depends(check_user)):
        if not user.is_superuser:
            raise HTTPException(status_code=403, detail="No superadmin")
        return user