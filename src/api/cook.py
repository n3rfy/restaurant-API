from ..models.cook import AllCookingOrderResponse
from ..services.cook import get_open_oreders

from fastapi import APIRouter

router = APIRouter(
    prefix='/cook',
    tags=['cook'],
)

@router.get('/', response_model= AllCookingOrderResponse)
async def get_open_orders():
    return await get_open_oreders()
