from pydantic import BaseModel

class AgriculturalMachineCreate(BaseModel):
    model_name: str
    manufacturer: str
    purchase_date: str
    commissioning_time: float

class AgriculturalMachineUpdate(BaseModel):
    model_name: str | None = None
    manufacturer: str | None = None
    purchase_date: str | None = None
    commissioning_time: float | None = None
