from pydantic import BaseModel
from typing import Optional

class AgriculturalMachine(BaseModel):
    id: int
    name: str
    type: str
    status: str
    location: Optional[str] = None
