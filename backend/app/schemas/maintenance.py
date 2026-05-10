from pydantic import BaseModel
from datetime import date

class MaintenanceHistoryCreate(BaseModel):
    machine_id: int
    maintenance_date: str
    description: str
    cost: float
    parts_used: list[int] | None = None

class MaintenanceHistoryUpdate(BaseModel):
    maintenance_date: str | None = None
    description: str | None = None
    cost: float | None = None
    parts_used: list[int] | None = None
