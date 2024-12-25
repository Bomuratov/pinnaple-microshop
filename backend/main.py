import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from api import router as router_v1
from bot.api import router as bot_router
from core import db_helper, settings
from bot import bot


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    logger.warning("————— Установка Webhook —————")
    await bot.set_webhook(f"{settings.bot_config.webhook_url}{settings.bot_config.webhook_path}{settings.bot_config.bot_token}")

    yield
    
    logger.warning("————— Удаляем Вебхук ————")    
    await bot.delete_webhook()
    logger.warning("————— Закрываем сессию БОТА ————")    
    await bot.session.close()
    logger.warning("————— Закрываем работу БД ————")    
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(router_v1)
main_app.include_router(bot_router)