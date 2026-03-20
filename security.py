# security.py
from fastapi import Header, HTTPException, status
import settings

def verify_api_key(x_api_key: str | None = Header(default=None)):
    expected = settings.API_KEY

    if expected is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API key not configured"
        )

    if x_api_key != expected:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key"
        )

    return True