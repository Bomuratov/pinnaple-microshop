from pydantic import BaseModel
from typing import Optional
from pydantic.types import UUID4


class UserAddEdit(BaseModel):
    username: str
    email: str
    phone: str
    password: str
    name: str
    surname: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_staff: Optional[bool]
    is_manager: Optional[bool]


class UserRead(UserAddEdit):
    id: int
    username: str
    email: str
    phone: str
    password: str
    name: str
    surname: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_staff: Optional[bool]


class UserEdit(BaseModel):
    username: str | None
    email: str | None
    phone: str | None
    name: str | None
    surname: str | None
    is_active: bool | None
    is_superuser: bool | None
    is_staff: bool | None
    is_manager: bool | None
