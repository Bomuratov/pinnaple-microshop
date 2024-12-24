from fastapi import status, HTTPException

class Unauthorized(HTTPException):
    def __init__(self, detail="Пользователь не авторизован"):
        super().__init__(status_code=401, detail=detail)


class Badcredentials(HTTPException):
    def __init__(self, detail="Неверные учетные данные"):
        super().__init__(status_code=400, detail=detail)