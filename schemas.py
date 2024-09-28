import uuid
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    id = int
    username = str
    email = str
    role_id = int
    is_active = Optional[bool] = True
    is_superuser = Optional[bool] = False
    is_verified = Optional[bool] = False


class UserCreate(schemas.BaseUserCreate):
    username= str
    email= str
    password= str
    role_id= int
    is_active = Optional[bool] = True
    is_superuser = Optional[bool] = False
    is_verified = Optional[bool] = False
