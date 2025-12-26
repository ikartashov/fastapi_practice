

class UserError(ValueError):
    pass

class UserLenNameError(UserError):
    pass

class UserAlreadyExistError(UserError):
    pass

class UserUpdateError(UserError):
    pass

class UserNotFoundError(UserError):
    pass

class UserDeleteError(UserError):
    pass

