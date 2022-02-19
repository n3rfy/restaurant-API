from ..models.order import ResponseFullOrder, CreateOrder
from ..services.waiter import ServiceWaiter 


from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/waiter',
    tags=['waiter'],
)

@router.post('/', response_model=ResponseFullOrder)
async def create_oreder(
    order: CreateOrder,
    service: ServiceWaiter = Depends(),
):
    return await service.create_order(order)
