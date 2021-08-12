from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional

from app.db.fake_users import fake_users_db
from app.models.user import User, UserInDB
from app.models.token import Token
from app.core.security import fake_hash_password
router = APIRouter()


@router.post("/", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(400, "Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(400, "Incorrect username or password")
    return {
        "access_token": user.username + "token!",
        "token_type": "bearer"
    }
