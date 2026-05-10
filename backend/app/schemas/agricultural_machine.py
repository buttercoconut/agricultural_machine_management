# app/schemas/agricultural_machine.py
from pydantic import BaseModel, Field
from datetime import date

class AgriculturalMachineBase(BaseModel):
    model_name: str
    manufacturer: str
    purchase_date: date
    commissioning_hours: float = 0.0

class AgriculturalMachineCreate(AgriculturalMachineBase):
    pass

class AgriculturalMachineUpdate(AgriculturalMachineBase):
    pass

class AgriculturalMachineInDBBase(AgriculturalMachineBase):
    id: int

    class Config:
        orm_mode = True

class AgriculturalMachine(AgriculturalMachineInDBBase):
    pass
