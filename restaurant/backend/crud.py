from sqlalchemy.orm import Session

import models, schemas

# Used in main to create a food item in the db table foods
def get_food_by_name(
        db: Session,
        name: str,
):
    return db.query(models.Food).filter(
        models.Food.name == name
    ).first()

def create_food(
        db: Session,
        food: schemas.FoodCreate
):
    db_food = models.Food(
        name=food.name, img_url=food.img_url, category=food.category, price=food.price,
    )
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

# Used in main to get all stored foods
def get_all_foods(
        db: Session,
        skip: int = 0,
        limit: int = 1000,
):
    return db.query(models.Food).offset(skip).limit(
        limit
    ).all()

# Used in main to create a table
def get_table_by_table_number(
        db: Session,
        table_number: int,
):
    return db.query(models.Table).filter(
        models.Table.table_number == table_number
    ).first()

def create_table(
        db: Session,
        table: schemas.TableCreate,
):
    db_table = models.Table(
        table_number=table.table_number
    )
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table

# Used in main to create an order
def create_order(
        db: Session,
        order: schemas.OrderCreate,
        food_id: int,
        table_id: int,
):
    db_order = models.Order(
        **order.model_dump(),
        food_id=food_id,
        table_id=table_id,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order