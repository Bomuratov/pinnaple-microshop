from fastapi import status, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from models import Product
from schemas.market.products_schema import ProductAdd, ProductEdit
import os
import random

UPLOAD_DIR = "media/uploads"

class ProductCRUD:
    def __init__(self) -> None:
        pass

    async def get_list(session: AsyncSession):
        state = select(Product).order_by(Product.id)
        result: Result = await session.execute(state)
        products = result.scalars().all()
        return list(products)
    
    async def create(payload: ProductAdd, photo: UploadFile, session: AsyncSession):
        file_extension = photo.filename.split(".")[-1]
        image_filename = f"{random.randint(0, 999999)}.{file_extension}"
        image_path = os.path.join(UPLOAD_DIR, image_filename)

        with open(image_path, "wb") as buffer:
            buffer.write(await photo.read())
        
        payload = payload.model_dump()
        payload["photo"] = image_path
        stmt = Product(**payload)
        session.add(stmt)
        await session.commit()
        await session.refresh(stmt)
        return stmt
    
    async def get(id: int, session: AsyncSession):
        stmt = select(Product).where(Product.id == id)
        result: Result = await session.execute(stmt)
        stmt = result.scalar_one_or_none()
        return stmt
    
    async def update(id: int, payload: ProductEdit, session: AsyncSession):
        result = await session.execute(select(Product).filter(Product.id == id))
        product = result.scalar_one_or_none()

        update_data = payload.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(product, key, value)

        await session.commit()
        await session.refresh(product)
        return product
        

    async def delete(id: int, session: AsyncSession):
        result = await session.execute(select(Product).filter(Product.id == id))
        product = result.scalar_one_or_none()
        await session.delete(product)
        await session.commit()
        return {"message": status.HTTP_204_NO_CONTENT}