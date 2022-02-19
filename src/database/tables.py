from sqlalchemy import (
    Column, 
    Table, 
    Integer, 
    String, 
    Numeric, 
    DateTime,
    ForeignKey,
    Boolean,
)
from .database import metadata
from datetime import datetime


staff = Table(
    "staff",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("role", String),
    Column("name", String),
    Column("salary", Numeric(10,2)),
    Column("login", String),
    Column("password", String),
)

order = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("status", String),
    Column("time_open", DateTime, default=datetime.utcnow),
    Column("time_close", DateTime, default=datetime.utcnow),
    Column("price", Numeric(10,2)),
    Column("waiter_id", ForeignKey("staff.id")),
    Column("cook_id", ForeignKey("staff.id")),
)

food = Table(
    "food",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True),
    Column("price", Numeric(10,2)),
)

orderfood = Table(
    "orderfood",
    metadata,
    Column('order_id', ForeignKey('order.id')),
    Column('food_id', ForeignKey('food.id')),
    Column('status', Boolean),
)

