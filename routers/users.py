from fastapi import APIRouter
from services.user_service import UserService
from schemas.user import UserCreate, UserRead, UserUpdate
from typing import List

router = APIRouter()
user_service = UserService()


@router.get('/get_users',
            response_model=List[UserRead])
def get_users():
    return user_service.get_users()


@router.post('/post_new_user',
             response_model=UserRead)
def add_user(user: UserCreate):
    return user_service.add_user(user.name)


@router.get('/get_user_by_id/{user_id}',
            response_model=UserRead)
def get_user_by_id(user_id: int):
    return user_service.get_user_by_id(user_id)


@router.get('/get_user_by_name/{name}',
            response_model=UserRead)
def get_user_by_name(name:str):
    return user_service.get_user_by_name(name)


@router.patch('/update_user/{user_id}',
              response_model=UserRead)
def update_user(user_id: int, new_name: UserUpdate):
    return user_service.update_user(user_id, new_name.name)


@router.delete('/delete_user/{user_id}',
               response_model=UserRead)
def delete_user(user_id: int):
    return user_service.delete_user(user_id)
