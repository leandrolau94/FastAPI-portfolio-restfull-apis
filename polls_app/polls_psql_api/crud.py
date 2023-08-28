from sqlalchemy.orm import Session

import models, schemas

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

# Used for get a certain question in main.py
def get_question_by_id(
        db: Session,
        question_id: int
):
    return db.query(models.Question).filter(
        models.Question.id == question_id
    ).first()

# Used for creating choices for a certain question
def get_question_choice_by_choice_text(
        db: Session,
        text: str,
        question_root_id: int
):
    return db.query(models.Choice).filter(
        models.Choice.choice_text == text,
        models.Choice.question_id == question_root_id,
    ).first()

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

# Used for updating (incrementing) the votes attributes
# for each choice of certain question
def get_question_choice_by_question_id_choice_id(
        db: Session,
        choice_id: int,
        question_root_id: int
):
    return db.query(models.Choice).filter(
        models.Choice.id == choice_id,
        models.Choice.question_id == question_root_id,
    ).first()