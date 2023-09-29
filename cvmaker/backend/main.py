from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from enum import Enum
import uvicorn

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Tags(Enum):
    persons = "persons"
    experience = "experience"
    skills = "skills"
    projects = "projects"
    languages = "languages"

# setting up cors policy
origins = [
    "http://192.168.43.163:3000",
    "http://localhost:3000",
    "http://0.0.0.0:8000",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # expose_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post(
    "/persons/",
    tags=[Tags.persons],
    response_model=schemas.Person,
    summary="Create a new person",
    include_in_schema=True,
)
def create_person(
    person: schemas.PersonCreate,
    db: Session = Depends(get_db)
):
    """
    Create a person with all its base information:

    - **full_name**: each person must have a human readable name
    - **email**: each person must have a contact email
    - **address**: each person must have a living address
    - **postal_code**: each person must have a postal code from its location
    - **phone_number**: each person must have a contact phone number
    """
    db_person = crud.get_person_by_email(db=db, email=person.email)
    if db_person:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return crud.create_person(db=db, person=person)

@app.get(
    "/persons/{person_id}",
    tags=[Tags.persons],
    response_model=schemas.Person,
    summary="Read a person by its id",
    include_in_schema=True,
)
def read_person(
    person_id: int,
    db: Session = Depends(get_db)
):
    """
    Read a person by its id

    - **full_name**: each person must have a human readable name
    - **email**: each person must have a contact email
    - **address**: each person must have a living address
    - **postal_code**: each person must have a postal code from its location
    - **phone_number**: each person must have a contact phone number
    - **work_experience**: each person must have a list of work experiences
    - **cv_skills**: each person must have a list of work skills
    - **cv_projects**: each person must have a list of projects for the cv
    - **cv_languages**: each person must have a list of languages for the cv
    """
    db_person = crud.get_person(db=db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    return db_person

@app.get(
    "/persons/",
    tags=[Tags.persons],
    response_model=list[schemas.Person],
    summary="Red all persons",
    include_in_schema=True,
)
def read_persons(skip: int = 0, limit: int = 10000, db: Session = Depends(get_db)):
    """
    Read all persons

    - **skip**: the lower bound for persons id
    - **limit**: the upper bound for persons id
    """
    persons = crud.get_persons(db=db, skip=skip, limit=limit)
    return persons

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )