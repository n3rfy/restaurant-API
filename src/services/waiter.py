from ..database.database import database
from ..models.order import ResponseFullOrder
from ..database.tables import order as order_t
from ..database.tables import orderfood

from datetime import datetime

class ServiceWaiter:

    def __init__(self) -> None:
        pass

    async def create_order(self, order):
        query = order_t.insert().values(
            status = order.status,
            waiter_id = order.waiter_id,
            time_open = datetime.utcnow(),
        )
        id = await database.execute(query)
        return ResponseFullOrder(id=id, **order.dict())
