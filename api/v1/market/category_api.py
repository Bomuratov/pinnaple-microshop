from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from crud.market import CategoryCRUD
from core import db_helper, settings
from schemas.market import CategoryGET, CategoryCreate

router = APIRouter(tags=["Category"],prefix=settings.api.v1.category, )

@router.post("/", response_model=CategoryGET)
async def brand_add(income: CategoryCreate, session: AsyncSession = Depends(db_helper.session_getter)):
    return await CategoryCRUD.create(name=income.name, session=session)

@router.get("/", response_model=List[CategoryGET])
async def brand_get_all(session: AsyncSession = Depends(db_helper.session_getter)):
    return await CategoryCRUD.get_list(session=session)

@router.get("/{id}", response_model=CategoryGET)
async def brand_get_id(id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    return await CategoryCRUD.get(id=id, session=session)

@router.put("/{id}", response_model=CategoryGET)
async def brand_update(income: CategoryCreate, id:int, session: AsyncSession = Depends(db_helper.session_getter)):
    return await CategoryCRUD.update(id=id, name=income.name, session=session)

@router.delete("/{id}")
async def brand_delete(id:int, session: AsyncSession = Depends(db_helper.session_getter)):
    return await CategoryCRUD.delete(id=id, session=session)