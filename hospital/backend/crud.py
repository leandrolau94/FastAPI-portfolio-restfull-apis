from sqlalchemy.orm import Session

import models, schemas

"""For patients basic crud"""

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

"""For anamnesis inform basic crud"""

# Used in main for creating the anamnesis report
# for a certain patient
def create_patient_anamnesis(
        db: Session,
        anamnesis: schemas.AnamnesisCreate,
        patient_id: int
):
    db_anamnesis = models.Anamnesis(
        **anamnesis.model_dump(),
        patient_id=patient_id,
    )
    db.add(db_anamnesis)
    db.commit()
    db.refresh(db_anamnesis)
    return db_anamnesis

# Used in main for get all anamnesis informs
# of all patients
def get_all_anamnesis(
        db: Session,
        skip: int = 0,
        limit: int = 1000000000000,
):
    return db.query(models.Anamnesis).offset(
        skip
    ).limit(limit).all()

"""For urgency inform basic crud"""

# Used in main for creating the urgency inform
# for a certain patient
def create_patient_urgency_inform(
        db: Session,
        urgency_inform: schemas.UrgencyInformCreate,
        patient_id: int,
):
    db_urgency_inform = models.UrgencyInform(
        **urgency_inform.model_dump(),
        patient_id=patient_id,
    )
    db.add(db_urgency_inform)
    db.commit()
    db.refresh(db_urgency_inform)
    return db_urgency_inform

# Used in main for get all the urgency informs
# of all patients
def get_all_urgency_informs(
        db: Session,
        skip: int = 0,
        limit: int = 1000000000000,
):
    return db.query(models.UrgencyInform).offset(
        skip
    ).limit(limit).all()