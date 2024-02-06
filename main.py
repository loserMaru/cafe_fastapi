from fastapi import FastAPI
from routes import cafe

app = FastAPI(
    title='Cafe API documentation'
)

app.include_router(cafe.router, prefix="/api")
