from fastapi import status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from models import Category


class CategoryCRUD:
    def __init__(self) -> None:
        pass

    async def get_list(session: AsyncSession):
        state = select(Category).order_by(Category.id)
        result: Result = await session.execute(state)
        categorys = result.scalars().all()
        return list(categorys)
    
    async def create(name: str, session: AsyncSession):
        stmt = Category(name=name)
        session.add(stmt)
        await session.commit()
        return stmt
    
    async def get(id: int, session: AsyncSession):
        stmt = select(Category).where(Category.id == id)
        result: Result = await session.execute(stmt)
        stmt = result.scalar_one_or_none()
        return stmt
    
    async def update(id: int, name: str, session: AsyncSession):
        result = await session.execute(select(Category).filter(Category.id == id))
        category = result.scalar_one_or_none()
        category.name=name
        await session.commit()
        return category
        

    async def delete(id: int, session: AsyncSession):
        result = await session.execute(select(Category).filter(Category.id == id))
        category = result.scalar_one_or_none()
        await session.delete(category)
        await session.commit()
        return {"message": status.HTTP_204_NO_CONTENT}