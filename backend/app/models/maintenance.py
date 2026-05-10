from pydantic import BaseModel
from datetime import date

class Maintenance(BaseModel):
    id: int
    machine_id: int
    maintenance_date: date
    description: str
    cost: float
