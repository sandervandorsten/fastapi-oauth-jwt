from fastapi import APIRouter, Depends

from app.api.deps import oauth2_scheme, get_current_user
from app.models.user import User

router = APIRouter()


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
