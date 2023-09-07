from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from sqlalchemy.orm import Session
import uvicorn

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )