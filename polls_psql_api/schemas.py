from pydantic import BaseModel

class ChoiceBase(BaseModel):
    choice_text: str
    votes_number: int = 0

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "choice_text": "Here goes the choice text",
                    "votes_number": 0,
                }
            ]
        }
    }

class ChoiceCreate(ChoiceBase):
    pass

class Choice(ChoiceBase):
    id: int
    question_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "choice_text": "Here goes the choice text",
                    "votes_number": 0,
                    "question_id": 2,
                }
            ]
        }
    }

    class Config:
        # for replacing the orm_mode = True
        from_attributes = True

class QuestionBase(BaseModel):
    question_text: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "question_text": "Here goes the question text",
                }
            ]
        }
    }

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    choices: list[Choice] = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 3,
                    "question_text": "Here goes the question text",
                    "choices": [
                        {
                            "id": 1,
                            "choice_text": "Here goes the choice text",
                            "votes_number": 0,
                            "question_id": 3,
                        },
                        {
                            "id": 2,
                            "choice_text": "Here goes the other choice text",
                            "votes_number": 2,
                            "question_id": 3,
                        },
                    ]
                }
            ]
        }
    }

    class Config:
        # for replacing the orm_mode = True
        from_attributes = True