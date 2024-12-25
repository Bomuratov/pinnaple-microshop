from fastapi import APIRouter

from .send_code import router as bot_router
from .webhook import router as webhook_router

router = APIRouter()

router.include_router(bot_router)
router.include_router(webhook_router)