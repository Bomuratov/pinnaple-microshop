from fastapi import Depends, APIRouter, Form
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Annotated
from enum import Enum

from core import settings, db_helper
from schemas.market import RoleAddEdit, RoleRead
from crud.market import UserRoleCRUD

router = APIRouter(tags=["User Roles"], prefix=settings.api.auth.role)

class UserRoles(str, Enum):
    admin = "admin"
    staff = "staff"
    manager = "manager"
    operator = "operator"

class Specific(str, Enum):
    add = "add"
    view = "view"
    update = "update"
    delete = "delete"

class Action(str, Enum):
    can = "can"

@router.post("/", response_model=RoleRead)
async def create_role(
    user_role: Annotated[UserRoles, Form(...)],  
    specific: Annotated[Specific, Form(...)],  
    action: Annotated[Action, Form(...)],  
    session: AsyncSession = Depends(db_helper.session_getter)):
    data = RoleAddEdit(user_role=user_role, specific=specific, action=action)
    return await UserRoleCRUD.create(data=data, session=session)

@router.get("/", response_model=List[RoleRead])
async def get_roles(session: AsyncSession = Depends(db_helper.session_getter)):
    return await UserRoleCRUD.get_list(session=session)

@router.get("/{id}", response_model=RoleRead)
async def get_role(id:int, session: AsyncSession=Depends(db_helper.session_getter)):
    return await UserRoleCRUD.get(id=id, session=session)