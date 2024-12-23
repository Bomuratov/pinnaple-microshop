from fastapi import HTTPException, status
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from typing import List
from models import Brand


class BrandCRUD:
    def __init__(self) -> None:
        pass

    async def get_list(session: AsyncSession):
        state = select(Brand).order_by(Brand.id)
        result: Result = await session.execute(state)
        brands = result.scalars().all()
        return list(brands)
    
    async def create(name: str, session: AsyncSession):
        stmt = Brand(name=name)
        session.add(stmt)
        await session.commit()
        return stmt
    
    async def get(id: int, session: AsyncSession):
        stmt = select(Brand).where(Brand.id == id)
        result: Result = await session.execute(stmt)
        stmt = result.scalar_one_or_none()
        return stmt
    
    async def update(id: int, name: str, session: AsyncSession):
        result = await session.execute(select(Brand).filter(Brand.id == id))
        brand = result.scalar_one_or_none()
        brand.name=name
        await session.commit()
        return brand
        

    async def delete(id: int, session: AsyncSession):
        result = await session.execute(select(Brand).filter(Brand.id == id))
        brand = result.scalar_one_or_none()
        await session.delete(brand)
        await session.commit()
        return {"message": status.HTTP_204_NO_CONTENT}