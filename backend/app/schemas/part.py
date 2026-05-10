from pydantic import BaseModel

class PartCreate(BaseModel):
    name: str
    quantity: int
    location: str

class PartUpdate(BaseModel):
    name: str | None = None
    quantity: int | None = None
    location: str | None = None
