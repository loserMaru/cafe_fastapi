from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy import select
from database import async_session
from database.models import CafeModel
from schemas.cafe_pydantic import Cafe, CafeCreate, CafeUpdate
from utils.middlewares import jwt_middleware

router = APIRouter(tags=['Cafe Routes'])
bearer = HTTPBearer()


@router.get("/list", response_model=List[Cafe], dependencies=[Depends(jwt_middleware)])
async def get_all_cafes():
    async with async_session() as session:
        async with session.begin():
            cafes = await session.execute(select(CafeModel))
            return cafes.scalars().all()


@router.post("", response_model=Cafe, dependencies=[Depends(jwt_middleware)])
async def create_cafe(cafe: CafeCreate):
    async with async_session() as session:
        async with session.begin():
            db_cafe = CafeModel(**cafe.dict())
            session.add(db_cafe)
            await session.commit()
        await session.refresh(db_cafe)
    return db_cafe


@router.get("/{id}", response_model=Cafe, dependencies=[Depends(jwt_middleware)])
async def get_cafe(id: int):
    async with async_session() as session:
        async with session.begin():
            cafe = await session.get(CafeModel, id)
            if cafe is None:
                raise HTTPException(status_code=404, detail="Cafe not found")
            return cafe


@router.put("/{id}", response_model=Cafe, dependencies=[Depends(jwt_middleware)])
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


@router.delete("/{id}", dependencies=[Depends(jwt_middleware)])
async def delete_cafe(id: int):
    async with async_session() as session:
        async with session.begin():
            db_cafe = await session.get(CafeModel, id)
            if db_cafe is None:
                raise HTTPException(status_code=404, detail="Cafe not found")
            await session.delete(db_cafe)
        await session.commit()
    return {"message": "Cafe deleted successfully"}
