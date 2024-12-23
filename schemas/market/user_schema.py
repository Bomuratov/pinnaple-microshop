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
    uuid: UUID4
    username: str
    email: str
    phone: str
    password: str
    name: str
    surname: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_staff: Optional[bool]

class UserGetByUUID(BaseModel):
    uuid: UUID4