from .database import metadata, database
from datetime import datetime

from typing import Optional, Union
import ormar

class Waiter(ormar.Model):
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    age: int = ormar.Integer(minimum=15)
    salary: float = ormar.Float(nullable=True)

class Cook(ormar.Model):
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    age: int = ormar.Integer(minimum=15)
    salary: float = ormar.Float()
   
class Food(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
    
    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    price: float = ormar.Float()

class OrderFood(ormar.Model):
    class Meta:
        tablename = "order_foods"
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    amount: int = ormar.Integer(default=1)

class Order(ormar.Model):
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    status: str = ormar.String(max_length=30, nullable=True)
    foods: Union[Food, list[Food]] = ormar.ManyToMany(
        Food, relation_name='orders', through=OrderFood
    )
    time_open: datetime = ormar.DateTime(default=datetime.utcnow())           
    time_close: Optional[datetime] = ormar.DateTime(nullable=True)
    waiter: Union[Waiter, dict] = ormar.ForeignKey(
        Waiter, relation_name='orders', name='waiter_id'
    )
    cook: Optional[Union[Cook, dict]] = ormar.ForeignKey(
        Cook, relation_name='orders', name='cook_id'
    )
