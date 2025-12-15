from fastapi import APIRouter, status, Depends
from bot.bot.commands import bot
from aiogram.exceptions import TelegramBadRequest
from backends.authorization import CheckUser



router = APIRouter(dependencies=[Depends(CheckUser.check_is_superuser)])
    

@router.post("/send_code/")
async def send_code(user_id: int, data: int ):
    
    try:
        await bot.send_message(chat_id=user_id, text=f"Ваш код верификации {data} не сообщите его никому. Данный код действителен в течении 15 минут", parse_mode="HTML")
        return {
            "status": status.HTTP_200_OK,
            "detail": "Success"
        }
    except TelegramBadRequest as e:
        return {
            "status": status.HTTP_403_FORBIDDEN,
            "detail": f"К сожалению мы не смогли отправить вам проверочный код пожалуйста войдите по ссылке и запустите бота https://t.me/verify_01_bot?start={user_id}"
        }