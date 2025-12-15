from fastapi import Depends, APIRouter, HTTPException, Form
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Annotated
from crud.market import UserCRUD
from core import db_helper, settings
from schemas.market import UserAddEdit, UserRead, UserEdit


router = APIRouter(tags=["Users"], prefix=settings.api.auth.user)

@router.post("/", response_model=UserRead)
async def user_add(data: Annotated[UserAddEdit, Form()], session: AsyncSession = Depends(db_helper.session_getter)):
    return await UserCRUD.create(session=session, data=data)

@router.get("/", response_model=List[UserRead])
async def user_get_list(session: AsyncSession = Depends(db_helper.session_getter)):
    return await UserCRUD.get_list(session)

@router.get("/{id}", response_model=UserRead)
async def user_get_by_id(id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    return await UserCRUD.get_by_id(id, session)

@router.put("/{id}", response_model=UserRead)
async def user_update(id: int, data: Annotated[UserEdit, Form()], session: AsyncSession = Depends(db_helper.session_getter)):
    return await UserCRUD.update(id, data, session)

