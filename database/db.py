from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

# URL вашей базы данных
DATABASE_URL = "postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
    DB_USER=DB_USER,
    DB_PASS=DB_PASS,
    DB_HOST=DB_HOST,
    DB_PORT=DB_PORT,
    DB_NAME=DB_NAME
)
# Создание асинхронного движка SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True, future=True, pool_size=20, max_overflow=0)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

database = async_session()
