from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

load_dotenv(dotenv_path=Path("~/.env"))

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class ApiAuthPrefix(BaseModel):
    prefix: str = "/auth"
    user: str = "/user"
    role: str = "/role"
    login: str = "/login"
    logout: str = "/logout"

class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"
    brand: str = "/brand"
    category: str = "/category"
    

class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()
    auth: ApiAuthPrefix = ApiAuthPrefix()


class TokenConfig(BaseModel):
    private_key: Path = BASE_DIR / "certificates" / "private.pem"
    public_key: Path = BASE_DIR / "certificates" / "public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15



class DatabaseConfig(BaseModel):
    url: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env"),
        case_sensitive=False,
        env_nested_delimiter="-",
        env_prefix="APP-CONFIG-",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig
    token_config: TokenConfig = TokenConfig()

settings = Settings()