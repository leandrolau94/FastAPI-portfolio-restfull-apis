from pydantic import BaseModel

class Choice(BaseModel):
    choice_text: str
    question_id: int

    class Config:
        orm_mode = True

class Question(BaseModel):
    question_text: str
    choices: list[Choice] = []

    class Config:
        orm_mode = True