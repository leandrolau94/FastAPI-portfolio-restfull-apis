from pydantic import BaseModel

class ChoiceBase(BaseModel):
    choice_text: str
    votes_number: int = 0

class ChoiceCreate(ChoiceBase):
    pass

class Choice(ChoiceBase):
    id: int
    question_id: int

    class Config:
        from_attributes = True

class QuestionBase(BaseModel):
    question_text: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    choices: list[Choice] = []

    class Config:
        from_attributes = True