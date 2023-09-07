from pydantic import BaseModel
import datetime

# For orders table
class OrderBase(BaseModel):
    quantity: int
    delivered: bool | None = False
    order_time: datetime.datetime = datetime.datetime.now()

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    food_id: int
    table_id: int

    class ConfigDict:
        # for replacing the orm_mode = True
        from_attributes = True

# For foods table
class FoodBase(BaseModel):
    name: str
    category: str
    price: float

class FoodCreate(FoodBase):
    pass

class Food(FoodBase):
    id: int
    orders: list[Order] = []

    class ConfigDict:
        # for replacing the orm_mode = True
        from_attributes = True

# For tables table
class TableBase(BaseModel):
    table_number: int

class TableCreate(TableBase):
    pass

class Table(TableBase):
    id: int
    table_orders: list[Order] = []

    class ConfigDict:
        # for replacing the orm_mode = True
        from_attributes = True