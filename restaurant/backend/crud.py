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
        name=food.name, category=food.category, price=food.price,
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