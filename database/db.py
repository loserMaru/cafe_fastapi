from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')

# URL вашей базы данных
DATABASE_URL = "mysql+aiomysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
    DB_USER=DB_USER,
    DB_PASS=DB_PASS,
    DB_HOST=DB_HOST,
    DB_PORT=DB_PORT,
    DB_NAME=DB_NAME
)
# Создание асинхронного движка SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True, future=True, pool_size=20, max_overflow=0)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
