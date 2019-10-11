from typing import List
from fastapi import APIRouter
from app.models.user import User, users_db


router = APIRouter()


@router.get('/', response_model=List[User])
async def read_users():
    return [User(**user) for user in users_db]


@router.get('/me', response_model=User)
async def read_user_me():
    user = next(user for user in users_db if user['id'] == 0)
    return User(**user)


@router.get('/{username}', response_model=User)
async def read_user(username: str):
    user = next(user for user in users_db if user['username'] == username)
    return User(**user)
