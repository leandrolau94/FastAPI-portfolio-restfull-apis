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
        name=food.name, price=food.price,
    )
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food