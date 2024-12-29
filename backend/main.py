import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from api import router as router_v1
from core import db_helper, settings
from authenticator.api.v1.send_code import router as router_bot
from authenticator.bot.commands import bot
from authenticator.bot.webhook import router as webhook


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Установка вебхук")
    webhook_url = f"{settings.bot_config.webhook_url}{settings.bot_config.webhook_path}{settings.bot_config.bot_token}"
    print("Webhook URL:", webhook_url)
    await bot.set_webhook(f"{settings.bot_config.webhook_url}{settings.bot_config.webhook_path}{settings.bot_config.bot_token}")
    yield
    await bot.delete_webhook()
    await bot.session.close()
    await db_helper.dispose()


fapp = FastAPI(lifespan=lifespan)
fapp.include_router(router_v1)
fapp.include_router(router_bot)
fapp.include_router(webhook)