# schemas/agricultural_machine.py
from datetime import date
from pydantic import BaseModel, Field

class AgriculturalMachineBase(BaseModel):
    model_name: str = Field(..., max_length=100)
    manufacturer: str = Field(..., max_length=100)
    purchase_date: date
    commissioning_time: float | None = None

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
