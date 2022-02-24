from ..database.tables import Order, Food
from ..core.exception import error

class ServiceWaiter:

    def __init__(self) -> None:
        pass
    
    @error
    async def create_order(self, order):
        ord = Order(
            **order.dict(exclude={'foods'}),
        )
        await ord.save()
        for food in order.dict().get('foods', []):
            food_id, amount = food['id'], food.get('amount')
            food = await Food.objects.get(pk=food_id)
            await ord.foods.add(food, amount=amount)

        ord = await (
            Order.objects.select_related(['foods'])
            .filter(id=ord.id)
            .first()
        )
        ord_dict = ord.dict()
        for count, food in enumerate(ord_dict['foods']):
            amount = food['orderfood']['amount']
            ord_dict['foods'][count]['amount'] = amount
            
        return ord_dict
    
    async def get_foods(self):
        foods = await Food.objects.all()
        return [ food.dict(exclude={'orders'}) for food in foods ]
    
     
