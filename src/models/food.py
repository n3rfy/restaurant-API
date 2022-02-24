from pydantic import BaseModel

class InfoFood(BaseModel):
    id: int
    name: str
    price: float

class AddFood(BaseModel):
    name: str 
    price: float
