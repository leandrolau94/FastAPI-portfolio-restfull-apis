from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# setting up cors policy
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # expose_headers=["*"],
)

# Dependency middleware
@app.middleware("http")
async def db_session_middleware(
    request: Request,
    call_next
):
    response = Response(
        "Internal Server Error",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Dependency
def get_db(request: Request):
    return request.state.db


# for create a food item in the foods database table
@app.post(
    "/food/",
    response_model=schemas.Food,
    summary="Create a food item with its name and price",
    include_in_schema=True,
)
def create_food(
    food: schemas.FoodCreate,
    db: Session = Depends(get_db),
):
    """
    Create a food item with its name, category and price to store it in database

    - **name**: The name of the food
    - **category**: The gastronomic category of the food
    - **price**: The price of the food
    """
    db_food = crud.get_food_by_name(
        db=db, name=food.name
    )
    if db_food:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Food already created",
        )
    return crud.create_food(
        db=db, food=food
    )

# for get all food items stored in the database
@app.get(
    "/food/",
    response_model=list[schemas.Food],
    summary="Get all food items in the database",
    include_in_schema=True,
)
def read_foods(
    skip: int = 0,
    limit: int = 1000,
    db: Session = Depends(get_db),
):
    """
    Get all food items in the database

    - **skip**: the lower bound for the id of the foods
    - **limit**: the upper bound for the id of the foods
    """
    foods = crud.get_all_foods(
        db=db, skip=skip, limit=limit,
    )
    return foods

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )