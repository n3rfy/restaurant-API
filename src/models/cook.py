from .order import CookingOrder, OpenOrder 
from pydantic import BaseModel


class AllCookingOrderResponse(BaseModel):
    data: list[CookingOrder]
    count_order: int

class AllOpenOrderResponse(BaseModel):
    data: list[OpenOrder]
    count_order: int

