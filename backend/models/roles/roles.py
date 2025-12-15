from sqlalchemy.orm import mapped_column
from sqlalchemy import String, event, Enum
from models import Basemodel
from enum import Enum as PyEnum


class UserRoles(String, PyEnum):
    admin = "admin"
    staff = "staff"
    manager = "manager"
    operator = "operator"


class Specific(String, PyEnum):
    add = "add"
    view = "view"
    update = "update"
    delete = "delete"


class Action(String, PyEnum):
    can = "can"


class UserRole(Basemodel):
    __tablename__ = "user_roles"

    user_role = mapped_column(Enum(UserRoles), nullable=False)
    specific = mapped_column(Enum(Specific), nullable=False)
    action = mapped_column(Enum(Action), nullable=False)
    assembled = mapped_column(String, nullable=False)

    def create_permission(self):
        return f"{self.user_role}_{self.action}_{self.specific}"


@event.listens_for(UserRole, "before_insert")
@event.listens_for(UserRole, "before_update")
def before_save_listener(mapper, connection, target):
    target.assembled = target.create_permission()
