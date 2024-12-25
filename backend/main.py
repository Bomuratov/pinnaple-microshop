from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from api import router as router_v1
from core import settings, db_helper



@asynccontextmanager
async def lifespan(app: FastAPI):


    yield
    print("Заканчиваем работу")
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(
    router_v1,
    )