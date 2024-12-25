import jwt
from datetime import timedelta, datetime
from core import settings




def encode(
    payload: dict,
    private_key: str = settings.token_config.private_key.read_text(),
    algorithm: str = settings.token_config.algorithm,
    expire_minutes: int = settings.token_config.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
) -> str:
    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm,
    )
    return encoded