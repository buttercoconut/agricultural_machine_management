# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from datetime import date

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str | None = None

class UserInDBBase(UserBase):
    id: int
    hashed_password: str
    created_at: date

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass
