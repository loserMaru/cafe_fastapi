from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from pydantic import BaseModel

from database.models import UserModel
from schemas.token_data import TokenData
from utils.security import verify_password, create_access_token, SECRET_KEY, ALGORITHM

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")


class Token(BaseModel):
    access_token: str
    token_type: str


@router.post("/login")
async def login(username: str, password: str):
    """Login and get access token"""
    user = await UserModel.get_by_email(username)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    # Generate JWT token
    access_token = create_access_token(
        data={"sub": user.email, "id": user.id, "role": user.role}
    )

    return Token(access_token=access_token, token_type="bearer")


@router.post("/refresh")
async def refresh_token():
    """Refresh access token"""
    # TODO: Implement refresh token logic
    raise HTTPException(status_code=501, detail="Not implemented")


async def get_current_user(token: str):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    return token_data


@router.get("/users/me")
async def read_users_me(current_user: TokenData = Depends(get_current_user)):
    return {"email": current_user.email}
