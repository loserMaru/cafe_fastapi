from fastapi import APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from database.db import engine
from database.models import CafeModel
from schemas.cafe_pydantic import Cafe, CafeCreate, CafeUpdate

router = APIRouter()

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


@router.get("/cafes/{id}", response_model=Cafe)
async def get_cafe(id: int):
    async with async_session() as session:
        async with session.begin():
            cafe = await session.get(CafeModel, id)
            if cafe is None:
                raise HTTPException(status_code=404, detail="Cafe not found")
            return cafe


@router.post("/cafes/", response_model=Cafe)
async def create_cafe(cafe: CafeCreate):
    async with async_session() as session:
        async with session.begin():
            db_cafe = CafeModel(**cafe.dict())
            session.add(db_cafe)
            await session.commit()
        await session.refresh(db_cafe)
    return db_cafe


@router.put("/cafes/{id}", response_model=Cafe)
async def update_cafe(id: int, cafe: CafeUpdate):
    async with async_session() as session:
        async with session.begin():
            db_cafe = await session.get(CafeModel, id)
            if db_cafe is None:
                raise HTTPException(status_code=404, detail="Cafe not found")
            for attr, value in cafe.dict(exclude_unset=True).items():
                setattr(db_cafe, attr, value)
            await session.commit()
            await session.refresh(db_cafe)
    return db_cafe


@router.delete("/cafes/{id}")
async def delete_cafe(id: int):
    async with async_session() as session:
        async with session.begin():
            db_cafe = await session.get(CafeModel, id)
            if db_cafe is None:
                raise HTTPException(status_code=404, detail="Cafe not found")
            session.delete(db_cafe)
            await session.commit()
    return {"message": "Cafe deleted successfully"}
