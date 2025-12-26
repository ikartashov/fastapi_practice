from exceptions import (
    UserLenNameError,
    UserAlreadyExistError,
    UserNotFoundError,
    UserDeleteError,
    map_user_error,
    http_error_mapper)
from repositories import user_repo_postgres
from sqlalchemy.exc import IntegrityError


class UserService:
    @http_error_mapper
    def add_user(self, name: str):
        if len(name) < 2 or len(name) > 50:
            raise UserLenNameError('Длина имени не соответствует')
        new_user = user_repo_postgres.add_user(name)
        if not new_user:
            raise UserAlreadyExistError('Пользователь с таким именем уже существует')
        return new_user

    @http_error_mapper
    def get_users(self):
        users = user_repo_postgres.get_users()
        return users

    @http_error_mapper
    def get_user_by_id(self, user_id: int):
        user_by_id = user_repo_postgres.get_user_by_id(user_id)
        if not user_by_id:
            raise UserNotFoundError('Пользователь не существует')
        return user_by_id

    @http_error_mapper
    def get_user_by_name(self, name: str):
        user_by_name = user_repo_postgres.get_user_by_name(name)
        if not user_by_name:
            raise UserNotFoundError('Пользователь не найден')
        return user_by_name

    @http_error_mapper
    def update_user(self, user_id: int, new_name: str):
        if len(new_name) < 2 or len(new_name) > 50:
            raise UserLenNameError('Длина нового имени не соответствует')
        try:
            updated_user = user_repo_postgres.update_user(user_id, new_name)
        except IntegrityError:
            raise UserAlreadyExistError('Пользователь с таким именем уже существует')
        if not updated_user:
            raise UserNotFoundError('Пользователь не найден')
        return updated_user

    @http_error_mapper
    def delete_user(self, user_id):
        deleted_user = user_repo_postgres.delete_user(user_id)
        if not deleted_user:
            raise UserDeleteError('Пользователь не найден или не может быть удалён')
        return deleted_user

