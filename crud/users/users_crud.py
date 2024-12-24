from fastapi import status, HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from models import UserModel
from schemas.market.user_schema import UserAddEdit, UserEdit



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
    
    async def update(id: int, data: UserEdit, session: AsyncSession):
        stmt = select(UserModel).where(UserModel.id == id)
        result = await session.execute(stmt)
        
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Not found")
        
        user = result.scalar_one_or_none()
        for key, value in data.model_dump().items():
            if value is not None:
                setattr(user, key, value)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
