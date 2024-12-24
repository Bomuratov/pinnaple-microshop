from fastapi import Form, Depends
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import UserValidate
from models import UserModel
from .exceptions import Unauthorized, Badcredentials
from core.utils import validate_password
from core import db_helper


async def validate_user(
        credentials: Annotated[UserValidate, Form(...)], 
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
        ):
    
    stmt = select(UserModel).where(UserModel.username == credentials.username)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise Unauthorized
    if not validate_password(password=credentials.password, hashed_password=user.password):
        raise Badcredentials
    print(user)
    return user