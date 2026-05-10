from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    role: str
    contact_info: str

class UserUpdate(BaseModel):
    name: str | None = None
    role: str | None = None
    contact_info: str | None = None
