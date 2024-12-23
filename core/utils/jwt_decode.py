import jwt
from core import settings


def decode(
    token: str | bytes,
    public_key : str = settings.token_config.public_key,
    algorithm : str = settings.token_config.algorithm,
):
    return jwt.decode(token, public_key, algorithms=[algorithm],)
