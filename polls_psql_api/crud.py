from sqlalchemy.orm import Session

from . import models, schemas

# Used for creating a new question in main.py
def create_question(
        db: Session,
        question: schemas.Question
):
    db_question = models.Question(
        question_text=question.question_text
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_question_by_question_text(
        db: Session,
        text: str
):
    return db.query(models.Question).filter(
        models.Question.question_text == text
    ).first()

# Used for get all questions in main.py
def get_all_questions(
        db: Session,
        skip: int = 0,
        limit: int = 100,
):
    return db.query(
        models.Question
    ).offset(skip).limit(limit).all()