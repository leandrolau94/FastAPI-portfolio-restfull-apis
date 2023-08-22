from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    question_text = Column(
        String,
        unique=True,
        index=True
    )

    choices = relationship(
        "Choice",
        back_populates="question_root"
    )

class Choice(Base):
    __tablename__ = "choices"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    choice_text = Column(
        String,
        unique=True,
        index=True
    )
    votes_number = Column(
        Integer,
        index=True
    )
    question_id = Column(
        Integer,
        ForeignKey("questions.id")
    )

    question_root = relationship(
        "Question",
        back_populates="choices"
    )