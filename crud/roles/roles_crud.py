from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from models import UserRole
from schemas.market import RoleAddEdit


class UserRoleCRUD:
    def __init__(self):
        pass

    async def create(data: RoleAddEdit, session:AsyncSession):
        stmt = UserRole(**data.model_dump())
        session.add(stmt)
        await session.commit()
        return stmt

    async def get_list(session: AsyncSession):
        stmt = select(UserRole).order_by(UserRole.id)
        result: Result = await session.execute(stmt)
        return list(result.scalars().all())
    
    async def get(id: int, session: AsyncSession):
        stmt = select(UserRole).where(UserRole.id == id)
        result: Result = await session.execute(stmt)
        return result.scalar_one_or_none()