from ..database.tables import Order, Food

from ..models.cook import AllOpenOrderResponse
from ..models.order import OpenOrder
from ..models.food import AddFood, InfoFood

class ServiceCook:
    def __init__(self) -> None:
        pass

    async def get_open_oreders(self) -> AllOpenOrderResponse:
        orders = await (
            Order.objects.select_related(['foods', 'waiter'])
            .filter(status='open')
            .all()
        )
        return AllOpenOrderResponse(
            data=[ OpenOrder(**order.dict()) for order in orders ],
            count_order=len(orders),
        )

    async def add_food(self, add_food: AddFood) -> InfoFood:
        food = Food(**add_food.dict())
        await food.save()
        return food
    
    async def delete_food(self, id_food: int) -> None:
        await Food.objects.delete(id=id_food)

