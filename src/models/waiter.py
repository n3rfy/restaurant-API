from .order import CreateOrder, StatusKind, BaseOrder, OpenOrder
from pydantic import BaseModel

class WaiterOpenInfo(BaseModel):
    id: int
    name: str

class WaiterCreateOrder(CreateOrder):
    waiter: int
    status: StatusKind = StatusKind('open')

class WaiterInfoOrder(OpenOrder):
    pass
