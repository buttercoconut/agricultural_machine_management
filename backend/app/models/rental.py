from pydantic import BaseModel
from datetime import date

class Rental(BaseModel):
    id: int
    machine_id: int
    renter_id: int
    start_date: date
    end_date: date
    daily_rate: float
