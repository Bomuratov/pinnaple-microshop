from pydantic import BaseModel


class RoleAddEdit(BaseModel):
    user_role: str
    specific: str
    action: str


class RoleRead(RoleAddEdit):
    id: int
    user_role: str
    specific: str
    action: str
    assembled: str
