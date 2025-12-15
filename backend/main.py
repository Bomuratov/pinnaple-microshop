from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from api import router as router_v1
from core import db_helper, settings
from bot.api import router as router_bot
from bot.bot.commands import bot
from bot.bot.webhook import router as webhook
from core.utils.logger import logger


origins = ["*"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Установка вебхук")
    await bot.set_webhook(f"{settings.bot_config.webhook_url}{settings.bot_config.webhook_path}{settings.bot_config.bot_token}")
    yield
    await bot.session.close()
    await db_helper.dispose()


fapp = FastAPI(lifespan=lifespan)
fapp.include_router(router_v1)
fapp.include_router(router_bot)
fapp.include_router(webhook, tags=["Webhook"])


fapp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)