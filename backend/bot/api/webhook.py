from fastapi import APIRouter
from aiogram import types
from core import settings
from bot import dispatcher, bot
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


class UpdateSchema(BaseModel):
    update_id: Optional[int]
    message: Optional[dict]

@router.post(f"{settings.bot_config.webhook_path}{settings.bot_config.bot_token}")
async def bot_webhook(update: UpdateSchema):
    print(update)
    update = types.Update(**update.dict())
    await dispatcher.feed_update(bot, update)
    