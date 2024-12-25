from aiogram.filters import Command
from aiogram import Bot, types, Dispatcher
from core import settings

bot = Bot(token=settings.bot_config.bot_token)
dispatcher = Dispatcher()


@dispatcher.message(Command("start"))
async def start(message: types.Message, bot: Bot):
    user_id = message.chat.id
    print(message)
    await bot.send_message(chat_id=user_id, text=f"Ваш id : {user_id}")