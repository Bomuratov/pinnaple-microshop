from fastapi import APIRouter
from core import settings
from .market.brand_api import router as brand_router
from .market.category_api import router as category_router
from .market.product_api import router as product_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(brand_router)
router.include_router(category_router)
router.include_router(product_router)
