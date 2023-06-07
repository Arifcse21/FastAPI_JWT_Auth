from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import os


class JWBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        is_valid_token: bool = False

        try:
            payload = jwt.decode(jwtoken, key=os.environ.get("SECRET"), algorithms=os.environ.get("ALGORITHM"))
        except:
            payload = None
        if payload:
            is_valid_token = True
        return is_valid_token