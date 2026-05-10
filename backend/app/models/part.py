from pydantic import BaseModel

class Part(BaseModel):
    id: int
    name: str
    quantity: int
    location: str
