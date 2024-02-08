from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from database import async_session
from database.models import UserModel
from schemas.user_pydantic import User, UserCreate, UserUpdate
from utils.security import hash_password

router = APIRouter(tags=['User Routes'])


@router.get("/list", response_model=List[User])
async def get_all_users():
    async with async_session() as session:
        async with session.begin():
            users = await session.execute(select(UserModel))
            return users.scalars().all()


@router.post("", response_model=User)
async def create_user(user: UserCreate):
    async with async_session() as session:
        async with session.begin():
            # Проверяем, существует ли пользователь с таким email
            existing_user = await session.execute(select(UserModel).where(UserModel.email == user.email))
            if existing_user.scalar_one_or_none():
                raise HTTPException(status_code=400, detail="User with this email already exists")

            # Устанавливаем значение по умолчанию для роли
            user_data = user.dict()
            user_data["role"] = "user"

            db_user = UserModel(**user_data)
            db_user.password = hash_password(user.password)
            session.add(db_user)
            await session.commit()
        await session.refresh(db_user)
    return db_user

@router.get("/{id}", response_model=User)
async def get_user(id: int):
    async with async_session() as session:
        async with session.begin():
            user = await session.get(UserModel, id)
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            return user


@router.put("/{id}", response_model=User)
async def update_user(id: int, user: UserUpdate):
    async with async_session() as session:
        async with session.begin():
            db_user = await session.get(UserModel, id)
            if db_user is None:
                raise HTTPException(status_code=404, detail="User not found")
            for attr, value in user.dict(exclude_unset=True).items():
                setattr(db_user, attr, value)
            await session.commit()
        await session.refresh(db_user)
    return db_user


@router.delete("/{id}")
async def delete_user(id: int):
    async with async_session() as session:
        async with session.begin():
            db_user = await session.get(UserModel, id)
            if db_user is None:
                raise HTTPException(status_code=404, detail="User not found")
            await session.delete(db_user)
        await session.commit()
    return {"message": "User deleted successfully"}
