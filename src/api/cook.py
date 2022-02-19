from ..models.cook import AllCookingOrderResponse


from fastapi import APIRouter

router = APIRouter(
    prefix='/cook',
    tags=['cook'],
)

@router.get('/', response_model= AllCookingOrderResponse)
async def get_open_orders():
    pass
