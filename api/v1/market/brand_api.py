from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from crud.market import BrandCRUD
from core import db_helper, settings
from schemas.market import BrandGet, BrandAddOrEdit

router = APIRouter(tags=["Brand"], prefix=settings.api.v1.brand,)

@router.post("/", response_model=BrandGet)
async def brand_add(income: BrandAddOrEdit, session: AsyncSession = Depends(db_helper.session_getter)):
    return await BrandCRUD.create(name=income.name, session=session)

@router.get("/", response_model=List[BrandGet])
async def brand_get_all(session: AsyncSession = Depends(db_helper.session_getter)):
    return await BrandCRUD.get_list(session=session)

@router.get("/{id}", response_model=BrandGet)
async def brand_get_id(id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    return await BrandCRUD.get(id=id, session=session)

@router.put("/{id}", response_model=BrandGet)
async def brand_update(income: BrandAddOrEdit, id:int, session: AsyncSession = Depends(db_helper.session_getter)):
    return await BrandCRUD.update(id=id, name=income.name, session=session)

@router.delete("/{id}")
async def brand_delete(id:int, session: AsyncSession = Depends(db_helper.session_getter)):
    return await BrandCRUD.delete(id=id, session=session)