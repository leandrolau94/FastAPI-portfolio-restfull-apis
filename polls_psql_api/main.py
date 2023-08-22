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

# Path operation for create a new question
@app.post(
    "/questions/",
    response_model=schemas.Question,
    summary="Create a question"
)
def create_question(
    question: schemas.QuestionCreate,
    db: Session = Depends(get_db)
):
    """
    Create a question with all the basic information:

    - **question_text**: Each question must have a text
    """
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

# Path operation for get all questions
@app.get(
    "/questions/",
    response_model=list[schemas.Question]
)
def read_all_questions(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    questions = crud.get_all_questions(
        db=db, skip=skip, limit=limit
    )
    return questions

# Path operation for create a choice for a
# certain question
@app.post(
    "/questions/{question_id}/choices/",
    response_model=schemas.Choice
)
def create_choice_for_question(
    question_id: int,
    choice: schemas.ChoiceCreate,
    db: Session = Depends(get_db)
):
    db_choice = crud.get_question_choice_by_choice_text(
        db=db,
        text=choice.choice_text,
        question_root_id=question_id
    )
    if db_choice:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Choice already exists"
        )
    return crud.create_question_choice(
        db=db,
        choice=choice,
        question_root_id=question_id
    )