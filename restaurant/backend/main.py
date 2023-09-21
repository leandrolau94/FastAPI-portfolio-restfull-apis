from fastapi import Depends, FastAPI, HTTPException, Request, Response, status, Path
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Annotated
import uvicorn

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# setting up cors policy
origins = [
    "http://192.168.43.163:3000",
    "http://192.168.43.163:3000/order",
    "http://localhost:3000",
    "http://localhost:3000/order",
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
    - **img_url**: The url of the image food sample
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

# For create a table in the tables database table
@app.post(
        "/table/",
        response_model=schemas.Table,
        summary="Create a table",
        include_in_schema=True,
)
def create_table(
    table: schemas.TableCreate,
    db: Session = Depends(get_db),
):
    """
    Create a table in the restaurant

    - **table_number**: The number of the table
    """
    db_table = crud.get_table_by_table_number(
        db=db, table_number=table.table_number
    )
    if db_table:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Table already exists"
        )
    return crud.create_table(db=db, table=table)

# For get all tables in the restaurant
@app.get(
        "/table/",
        response_model=list[schemas.Table],
        summary="Get all tables in the restaurant",
        include_in_schema=True,
)
def read_tables(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """
    Get all tables in the restaurant

    - **skip**: lower bound for tables id
    - **limit**: upper bound for tables id
    """
    tables = crud.get_all_tables(
        db=db, skip=skip, limit=limit,
    )
    return tables

# For getting a table by its table_id
@app.get(
        "/table/{table_id}",
        response_model=schemas.Table,
        summary="Get a table by its table id",
        include_in_schema=True,
)
def read_table_by_table_id(
    table_id: int,
    db: Session = Depends(get_db),
):
    db_table = crud.get_table_by_table_id(
        db=db, table_id=table_id
    )
    if db_table is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Table not found",
        )
    return db_table

# For delete all orders from a certain table
@app.delete(
        "/table/{table_id}/delete-order",
        summary="Delete all orders from a table",
        include_in_schema=True,
)
def delete_order_from_table_id(
    table_id: int,
    db: Session = Depends(get_db),
):
    return crud.delete_order_from_table_id(
        db=db, table_id=table_id
    )

# For create an order in the order database table
@app.post(
    "/order/food/{food_id}/table/{table_id}/",
    response_model=schemas.Order,
    summary="Create an order in the database",
    include_in_schema=True,
)
def create_order(
    food_id: Annotated[int, Path(title="The id of the food to order", gt=0)],
    table_id: Annotated[int, Path(title="The id of the table the order comes from", gt=0)],
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
):
    """
    Create an order for the kitchen

    - **food_id**: The id of the food to order
    - **table_id**: The id of the restaurant table the order comes from
    - `quantity`: The quantity of food per order
    """
    return crud.create_order(
        db=db,
        order=order,
        food_id=food_id,
        table_id=table_id,
    )

# For get all orders in the order database table
@app.get(
    "/order/",
    response_model=list[schemas.Order],
    summary="Get all orders in the restaurant",
    include_in_schema=True,
)
def read_orders(
    skip: int = 0,
    limit: int = 1000000,
    db: Session = Depends(get_db),
):
    """
    Get all orders in the restaurant

    - **skip**: lower bound for orders id
    - **limit**: upper bound for orders id
    """
    orders = crud.get_all_orders(
        db=db, skip=skip, limit=limit
    )
    return orders

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )