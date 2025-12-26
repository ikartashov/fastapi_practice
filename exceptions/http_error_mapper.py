from fastapi import HTTPException

from exceptions.user_error import UserLenNameError, UserAlreadyExistError, UserUpdateError, UserNotFoundError, UserDeleteError

ERROR_MAP={
    UserLenNameError:422,
    UserAlreadyExistError: 409,
    UserUpdateError:400,
    UserNotFoundError:404,
    UserDeleteError:404
}
def map_user_error(exc: Exception):
    status_code = ERROR_MAP.get(type(exc))
    if status_code:
        raise HTTPException(
            status_code=status_code,
            detail=str(exc))
    raise exc

def http_error_mapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            map_user_error(exc)
    return wrapper



