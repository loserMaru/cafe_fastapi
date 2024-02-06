from sqlalchemy.ext.asyncio import AsyncSession


async def create(session: AsyncSession, model, data):
    db_model = model(**data.dict())
    session.add(db_model)
    await session.commit()
    return db_model


async def get(session: AsyncSession, model, model_id):
    return await session.get(model, model_id)
