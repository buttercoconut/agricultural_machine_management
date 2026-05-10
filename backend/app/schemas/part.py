# app/schemas/part.py
from pydantic import BaseModel, Field

class PartBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock_quantity: int = 0

class PartCreate(PartBase):
    pass

class PartUpdate(PartBase):
    pass

class PartInDBBase(PartBase):
    id: int

    class Config:
        orm_mode = True

class Part(PartInDBBase):
    pass
