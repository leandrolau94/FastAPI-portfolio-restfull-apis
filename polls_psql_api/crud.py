from sqlalchemy.orm import Session

from . import models, schemas

# Used for creating a new question in main.py
def create_question(
        db: Session,
        question: schemas.QuestionCreate
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

# Used for creating choices for a certain question
def create_question_choice(
        db: Session,
        choice: schemas.ChoiceCreate,
        question_root_id: int
):
    db_choice = models.Choice(
        **choice.model_dump(),
        question_id=question_root_id
    )
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice