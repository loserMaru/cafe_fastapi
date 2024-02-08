import uvicorn
from fastapi import FastAPI
from routes import cafe, user

app = FastAPI(
    title='Cafe API documentation',
    description='Cafe API',
    name='Cafe API',
)

app.include_router(cafe.router, prefix="/api/cafes")
app.include_router(user.router, prefix="/api/users")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
