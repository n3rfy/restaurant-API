from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class StatusKind(str, Enum):
    OPEN = 'open'
    COOKING = 'cooking'
    CLOSE = 'close'

class Food(BaseModel):
    id: int
    name: str
    price: float
    amount: int

class OrderFood(BaseModel):
    id: int = Field(..., gt=0)
    amount: int = Field(..., gt=0)

class CreateOrder(BaseModel):
    foods: list[OrderFood]

class ResponseFullCloseOrder(BaseModel):
    id: int
    status: StatusKind
    foods: list[Food]
    time_open: datetime
    time_close: Optional[datetime]
    price: float

class BaseOrder(BaseModel):
    id: int
    foods: list[Food]
    time_open: datetime

class OpenOrder(BaseOrder):
    status: StatusKind = StatusKind('open')

class CookingOrder(BaseOrder):
    status: StatusKind = StatusKind('cooking')

class CloseOrder(BaseOrder):
    status: StatusKind = StatusKind('close')
    time_close: datetime
    
