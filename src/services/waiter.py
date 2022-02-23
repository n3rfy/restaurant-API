from ..database.tables import Order, Food

class ServiceWaiter:

    def __init__(self) -> None:
        pass

    async def create_order(self, order):
        ord = Order(**order.dict(exclude={'foods'}))
        await ord.save()
        food = await Food.objects.get(id=order.dict().pop('foods')[0])
        await ord.foods.add(food)
        return ord
