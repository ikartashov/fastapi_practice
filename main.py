from fastapi import FastAPI
import uvicorn
from routers import users

app = FastAPI(title='Практика FastAPI с Postgres на Docker')

app.include_router(users.router,
                   prefix='/users',
                   tags=['Пользователи'])


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)

# Импорты и прочее до изменения архитектуры
# from models import User
# from services import UserService
# from db_sqlite import create_table
# from services_for_postgres import UserService
# create_table()
# user_service = UserService()


# Ручки для использования с Postgres
# @app.post('/add_new_use',
#           tags=['Добавить нового пользователя'])
# def add_user(name: str):
#     try:
#         new_user = user_service.add_user(name)
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     return new_user
#
#
# @app.get('/get_from_postgres',
#          tags=['Получить пользователей'],
#          summary='Получить всех пользователей')
# def get_users_endpoint():
#     return user_service.get_users()
#
#
# @app.get('/get_from_postgres/{user_id}',
#          tags=['Получить конкретного пользователя'],
#          summary='Получить пользователя по id')
# def get_user_by_id_endpoint(user_id: int):
#     try:
#         user = user_service.get_user_by_id(user_id)
#
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
#     return user
#
#
# @app.get('/get_from_postgres/by_name/{name}',
#          tags=['Получить конкретного пользователя'],
#          summary='Получить пользователя по имени')
# def get_user_by_name(name: str):
#     try:
#         user = user_service.get_user_by_name(name)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
#     return user
#
#
# @app.patch('/update_user/{user_id}',
#            tags=['Изменить конкретного пользователя'],
#            summary='Изменить пользователя по id')
# def update_user(user_id:int, new_name:str):
#     try:
#         updated_user = user_service.update_user(user_id, new_name)
#     except ValueError as e:
#         raise HTTPException(status_code= 404, detail=str(e))
#     return updated_user
#
# @app.delete('/delete_user/{user_id}',
#             tags=['Удалить конкретного пользователя'],
#             summary='Удалить пользователя по id')
# def delete_user(user_id:int):
#     try:
#         deleted_user= user_service.delete_user(user_id)
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))
#     return deleted_user


# Ручки для использования с SQLite
# @app.get('/get',
#          tags=['Получить пользователей'],
#          summary='Получить всех пользователей')
# def get_users():
#     return user_service.get_users()
#
#
# @app.get('/get/user_by_id',
#          tags=['Получить пользователей'],
#          summary='Получить конкретного пользователя')
# def get_user_by_id(user_id: int):
#     try:
#         user = user_service.get_user_by_id(user_id)
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     return user
#
#
# @app.post('/post',
#           response_model=list,
#           tags=['Добавить нового пользователя'],
#           summary='Добавить пользователя')
# def post_users(new_user: User):
#     try:
#         user_service.add_user(new_user.name)
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     return user_service.get_users()
#
# @app.patch('/patch',
#            tags=['Обновить пользователя'],
#            summary='Обновить пользователя')
# def update_user(user_id, new_name):
#     try:
#         new_user = user_service.update_user(user_id, new_name)
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     return new_user
#
# @app.delete('/delete/{user_id}',
#             tags=['Удалить пользователя'],
#             summary='Удалить пользователя')
# def delete_user(user_id:int):
#     try:
#         deleted_user = user_service.delete_user(user_id)
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     return deleted_user
