from fastapi import APIRouter

from core import settings
from .v1 import router as router_api_v1
from .authentication import router as authrouter

router = APIRouter(
    prefix=settings.api.prefix,
)
router.include_router(router_api_v1)
router.include_router(authrouter)