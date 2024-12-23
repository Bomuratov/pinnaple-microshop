from fastapi import status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from models import UserModel
from schemas.market import UserAddEdit, UserRead, UserGetByUUID
from pydantic.types import UUID4



class UserCRUD:
    def __init__(self):
        pass

    async def create(data: UserAddEdit, session: AsyncSession):
        stmt = UserModel(**data.model_dump())
        session.add(stmt)
        await session.commit()
        return stmt
    
    async def get_list(session: AsyncSession):
        stmt = select(UserModel).order_by(UserModel.id)
        result: Result = await session.execute(stmt)
        print(result)
        return list(result.scalars().all())
    
    async def get_by_id(id: int, session: AsyncSession):
        stmt = select(UserModel).where(UserModel.id == id)
        result: Result = await session.execute(stmt)
        stmt = result.scalar_one_or_none()
        return stmt
    
    async def get_by_uuid(uuid: UserGetByUUID, session: AsyncSession):
        stmt = select(UserModel).where(UserModel.uuid == uuid)
        result: Result = await session.execute(stmt)
        return result.scalar_one_or_none()