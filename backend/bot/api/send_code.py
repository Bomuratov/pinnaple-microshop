from fastapi import APIRouter, status
from bot import bot


router = APIRouter(prefix="/api/v1/bot/send_code", tags=["Notify bot"])

user_id = {
    "id": 5092708098
}

@router.post("/")
async def send_message_to_user(user_id: int, data: int ):
    await bot.send_message(chat_id=user_id, text=f"Ваш код верификации {data} не сообщите его никому. Данный код действителен в течении 15 минут", parse_mode="HTML")
    return {
        "status": status.HTTP_200_OK,
        "detail": "Success"
        }