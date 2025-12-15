from fastapi import APIRouter
from .v1 import router as router_v1
from core import settings

router = APIRouter(prefix=settings.api.prefix, tags=["Bot API"])

router.include_router(router_v1)