from fastapi import APIRouter
from core import settings
from .users_api import router as user_router
from .roles_api import router as role_router
from .authentication import router as auth_router
from .verification import router as verify_router

router = APIRouter(
    prefix=settings.api.auth.prefix
)

router.include_router(user_router)
router.include_router(role_router)
router.include_router(auth_router)
router.include_router(verify_router)