from aiogram import Bot, Dispatcher
from core import settings

bot = Bot(token=settings.bot_config.bot_token)
dispatcher = Dispatcher()