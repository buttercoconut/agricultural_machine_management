# app/schemas/maintenance.py
from pydantic import BaseModel, Field
from datetime import date

class MaintenanceBase(BaseModel):
    machine_id: int
    maintenance_date: date
    description: str
    cost: float = 0.0
    parts_replaced: str | None = None

class MaintenanceCreate(MaintenanceBase):
    pass

class MaintenanceUpdate(MaintenanceBase):
    pass

class MaintenanceInDBBase(MaintenanceBase):
    id: int

    class Config:
        orm_mode = True

class Maintenance(MaintenanceInDBBase):
    pass
