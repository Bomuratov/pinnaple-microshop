from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, TYPE_CHECKING
from backends.authorization import CheckUser
from crud.market import BrandCRUD
from core import db_helper, settings
from schemas.market import BrandGet, BrandAddOrEdit
from models import UserModel


    

router = APIRouter(tags=["Brand"], prefix=settings.api.v1.brand, dependencies=[Depends(CheckUser.check_user)])

@router.post("/", response_model=BrandGet)
async def brand_add(income: BrandAddOrEdit, session: AsyncSession = Depends(db_helper.session_getter), user: UserModel = Depends(CheckUser.check_is_superuser)):
    return await BrandCRUD.create(name=income.name, session=session)

@router.get("/", response_model=List[BrandGet])
async def brand_get_all(session: AsyncSession = Depends(db_helper.session_getter), user: UserModel = Depends(CheckUser.check_is_manager)):
    return await BrandCRUD.get_list(session=session)

@router.get("/{id}", response_model=BrandGet)
async def brand_get_id(id: int, session: AsyncSession = Depends(db_helper.session_getter), user: UserModel = Depends(CheckUser.check_is_superuser)):
    return await BrandCRUD.get(id=id, session=session)

@router.put("/{id}", response_model=BrandGet)
async def brand_update(income: BrandAddOrEdit, id:int, session: AsyncSession = Depends(db_helper.session_getter), user: UserModel = Depends(CheckUser.check_is_superuser)):
    return await BrandCRUD.update(id=id, name=income.name, session=session)

@router.delete("/{id}")
async def brand_delete(id:int, session: AsyncSession = Depends(db_helper.session_getter), user: UserModel = Depends(CheckUser.check_is_superuser)):
    return await BrandCRUD.delete(id=id, session=session)