from fastapi import APIRouter, Depends, Form, UploadFile, File, Body
from sqlalchemy.ext.asyncio import AsyncSession
from core import settings, db_helper
from crud.market.product_crud import ProductCRUD
from schemas.market.products_schema import ProductAdd, ProductEdit, ProductGet
from typing import List, Annotated

router = APIRouter(tags=["Product"], prefix=settings.api.v1.product)


@router.get("/", response_model=List[ProductGet])
async def get_product_list(session: AsyncSession = Depends(db_helper.session_getter)):
    return await ProductCRUD.get_list(session)


@router.post("/", response_model=ProductGet)
async def add_product(payload: ProductAdd = Body(...), photo: UploadFile = File(...), session: AsyncSession = Depends(db_helper.session_getter)):
    return await ProductCRUD.create(payload=payload, photo=photo, session=session)


@router.delete("/{id}")
async def delete_product(id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    return await ProductCRUD.delete(id, session)