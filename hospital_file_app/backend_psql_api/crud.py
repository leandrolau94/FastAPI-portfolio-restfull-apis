from sqlalchemy.orm import Session

import models, schemas

# Used in main for the create patient
# path operation
def get_patient_by_dni(
        db: Session,
        dni: str
):
    return db.query(models.Patient).filter(
        models.Patient.dni == dni
    ).first()

def create_patient(
        db: Session,
        patient: schemas.PatientCreate
):
    db_patient = models.Patient(
        full_name=patient.full_name,
        email=patient.email,
        genre=patient.genre,
        age=patient.age,
        address=patient.address,
        dni=patient.dni,
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

# Used in main for the get all patients
# path operation
def get_all_patients(
        db: Session,
        skip: int = 0,
        limit: int = 1000000000
):
    return db.query(models.Patient).offset(
        skip
    ).limit(limit).all()

# Used in main for get a patient by its id
def get_patient_by_id(
        db: Session,
        patient_id: int
):
    return db.query(models.Patient).filter(
        models.Patient.id == patient_id
    ).first()