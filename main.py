import uvicorn
from fastapi import FastAPI
from routes import cafe, user, auth

app = FastAPI(
    title='Cafe API documentation',
    description='Cafe API',
    name='Cafe API',
)

app.include_router(cafe.router, prefix="/api/cafes")
app.include_router(user.router, prefix="/api/users")
app.include_router(auth.router, prefix="/api/auth")

if __name__ == "__main__":
    uvicorn.run(app, reload=True)
