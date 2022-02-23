from pydantic import BaseModel
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
class CreateOrder(BaseModel):
    status = 'open'
    foods: list[int]
    waiter: int
    price: float

class ResponseFullOrder(BaseModel):
    id: int
    status: StatusKind
    foods: list[Food]
    time_open: datetime
    time_close: Optional[datetime]
    price: float
    waiter_id: int
    cook_id: Optional[int]

class BaseOrder(BaseModel):
    id: int
    foods: list[Food]
    time_open: datetime
    price: float
    waiter_id: int

class OpenOrder(BaseOrder):
    status = 'open'

class CookingOrder(BaseOrder):
    status = 'cooking'
    cook_id: int

class CloseOrder(BaseOrder):
    status = 'close'
    cook_id: int
    time_close: datetime
    
