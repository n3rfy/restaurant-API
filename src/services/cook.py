from ..database.tables import Order
from ..models.cook import AllOpenOrderResponse


async def get_open_oreders():
     orders = await Order.objects.select_all().filter(status='open').all()
     return AllOpenOrderResponse(
        data=orders,
        count_order=len(orders),
    )
