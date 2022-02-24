from ..models.waiter import WaiterCreateOrder, WaiterInfoOrder
from ..models.food import InfoFood
from ..services.waiter import ServiceWaiter 

from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/waiter',
    tags=['waiter'],
)

@router.post('/', response_model=WaiterInfoOrder)
async def create_oreder(
    order: WaiterCreateOrder,
    service: ServiceWaiter = Depends(),
):
    return await service.create_order(order)

@router.get('/foods', response_model=list[InfoFood])
async def get_foods(
    service: ServiceWaiter = Depends(),
):
    return await service.get_foods()
