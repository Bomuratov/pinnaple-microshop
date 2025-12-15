from fastapi import APIRouter
from .send_code import router as send_code_router
from core import settings

router = APIRouter(prefix=settings.api.v1.prefix)
router.include_router(send_code_router)