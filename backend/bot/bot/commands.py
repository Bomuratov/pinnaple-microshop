from sqlalchemy import select
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from core import settings, db_redis

bot = Bot(token=f"{settings.bot_config.bot_token}")
dp = Dispatcher()

@dp.message(Command("start"))
async def send_message(message: types.Message):
    phone_id = message.text[7:]
    if not phone_id:
        return await bot.send_message(chat_id=message.chat.id,
                                      text="По вашему номеру телефона не найден проверочный код. Для решения проблемы обратитесь в поддержку",
                                      parse_mode="HTML")
    redis_key = f"verification:{phone_id}"
    code = db_redis.get(redis_key)

    if not code:
        return await bot.send_message(chat_id=message.chat.id,
                                      text="Вашему номеру телефона пока неназначен проверочный код. Для решения проблемы обратитесь в поддержку",
                                      parse_mode="HTML")
    code = code.decode('utf-8') if isinstance(code, bytes) else code
    return await bot.send_message(chat_id=message.chat.id, 
                                  text=f"Ваш код верификации {code} не сообщите его никому. Данный код действителен в течении 15 минут", 
                                  parse_mode="HTML")
