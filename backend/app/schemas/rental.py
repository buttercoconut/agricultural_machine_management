from pydantic import BaseModel
from datetime import date

class RentalCreate(BaseModel):
    machine_id: int
    renter_id: int
    start_date: str
    end_date: str
    rental_fee: float

class RentalUpdate(BaseModel):
    start_date: str | None = None
    end_date: str | None = None
    rental_fee: float | None = None
