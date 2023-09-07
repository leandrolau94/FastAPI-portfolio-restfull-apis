import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, index=True)
    delivered = Column(Boolean, default=False)
    order_time = Column(DateTime, default=datetime.datetime.now())
    food_id = Column(Integer, ForeignKey(
        'foods.id',
        ondelete='CASCADE',
    ))
    table_id = Column(Integer, ForeignKey(
        'tables.id',
        ondelete='CASCADE',
    ))

    foods = relationship(
        "Food",
        back_populates="orders",
    )
    tables = relationship(
        "Table",
        back_populates="table_orders",
    )

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category = Column(String, index=True)
    price = Column(Float, index=True)

    orders = relationship(
        "Order",
        back_populates="foods",
    )

class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    table_number = Column(Integer, index=True)

    table_orders = relationship(
        "Order",
        back_populates="tables",
    )