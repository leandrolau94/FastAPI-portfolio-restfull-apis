from pydantic import BaseModel

class ChoiceBase(BaseModel):
    choice_text: str

class ChoiceCreate(ChoiceBase):
    pass

class Choice(ChoiceBase):
    id: int
    question_id: int

    class Config:
        orm_mode = True

class Question(BaseModel):
    question_text: str
    choices: list[Choice] = []

    class Config:
        orm_mode = True