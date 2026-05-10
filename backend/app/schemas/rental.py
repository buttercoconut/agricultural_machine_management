# app/schemas/rental.py
from pydantic import BaseModel, Field
from datetime import date

class RentalBase(BaseModel):
    machine_id: int
    renter_name: str
    start_date: date
    end_date: date
    daily_rate: float

class RentalCreate(RentalBase):
    pass

class RentalUpdate(RentalBase):
    pass

class RentalInDBBase(RentalBase):
    id: int
    total_cost: float

    class Config:
        orm_mode = True

class Rental(RentalInDBBase):
    pass
