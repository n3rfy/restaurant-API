from ..models.cook import AllCookingOrderResponse, AllOpenOrderResponse
from ..services.cook import ServiceCook 
from ..models.food import InfoFood, AddFood

from fastapi import APIRouter, Depends, Response

router = APIRouter(
    prefix='/cook',
    tags=['cook'],
)

@router.get('/', response_model=AllOpenOrderResponse)
async def get_open_orders(
    service: ServiceCook = Depends()
) -> AllOpenOrderResponse:
    return await service.get_open_oreders()

@router.post('/food', response_model=InfoFood)
async def add_food(
    food: AddFood,
    service: ServiceCook = Depends(),
) -> InfoFood:
    return await service.add_food(food)

@router.delete(
    '/food/{pk}', 
    status_code=204,
    response_class=Response
)
async def delete_food(
    pk: int,
    service: ServiceCook = Depends(),
):
    await service.delete_food(id_food=pk)
