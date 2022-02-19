from ..database.database import database
from ..database.tables import order as order_t



async def get_open_oreders():
    query = order_t.select().where(order_t.c.status == 'open')
    res = await database.fetch_all(query)
    print(res)
