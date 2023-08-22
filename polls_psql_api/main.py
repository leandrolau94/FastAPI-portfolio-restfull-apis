from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post(
    "/questions/",
    response_model=schemas.Question
)
def create_question(
    question: schemas.Question,
    db: Session = Depends(get_db)
):
    db_question = crud.get_question_by_question_text(
        db=db,
        text=question.question_text
    )
    if db_question:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Question already created"
        )
    return crud.create_question(
        db=db, question=question
    )