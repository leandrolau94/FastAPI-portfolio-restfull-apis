from sqlalchemy.orm import Session

import models, schemas

# Used in main for reading a person endpoint
def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(
        models.Person.id == person_id
    ).first()

# Used in main for creating person endpoint
def get_person_by_email(db: Session, email: str):
    return db.query(models.Person).filter(
        models.Person.email == email
    ).first()

def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(full_name=person.full_name, email=person.email, address=person.address, postal_code=person.postal_code, phone_number=person.phone_number)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

# Used in main for reading all persons
def get_persons(db: Session, skip: int = 0, limit: int = 10000):
    return db.query(models.Person).offset(skip).limit(limit).all()