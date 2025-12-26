from pydantic import BaseModel, Field, ConfigDict


class UserCreate(BaseModel):
    name: str = Field(description='Имя пользователя')


class UserRead(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    name: str = Field(description='Имя пользователя')
