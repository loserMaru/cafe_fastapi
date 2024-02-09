from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from utils.security import SECRET_KEY


async def jwt_middleware(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    try:
        token = credentials.credentials
        decoded_token = jwt.decode(token,  SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
