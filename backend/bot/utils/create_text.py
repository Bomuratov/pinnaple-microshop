from api.v1.market.verification import VerifyCode

def body_text(data: VerifyCode):
    return f"Ваш код верификации {VerifyCode.code} не сообщите его никому. Данный код действителен в течении 15 минут"