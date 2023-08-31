from fastapi import FastAPI, Depends, HTTPException, Request, Response, status

from sqlalchemy.orm import Session

from database import engine, SessionLocal
import models, crud, schemas

from routers.patients import patients_router
from routers.anamnesis import anamnesis_router
from routers.urgency_informs import urgency_informs_router

import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(
    request: Request,
    call_next
):
    response = Response(
        "Internal Server Error",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Dependency
def get_db(request: Request):
    return request.state.db

""" Section for path operations router with patients"""

# Patient router operation for create a patient
@patients_router.post(
    "/create",
    response_model=schemas.Patient,
    summary="Create a patient",
    include_in_schema=True,
)
def create_patient(
    patient: schemas.PatientCreate,
    db: Session = Depends(get_db),
):
    """
    Create a patient with all its basic identification information

    - **full_name**: each patient must have a full name
    - **email**: each patient must have an email for contact purposes
    - **genre**: each patient must have a genre
    - **age**: each patient must have an certain age
    - **address**: each patient must have an address
    - **dni**: each patient must have a unique dni to be a legal spanish citizen
    \f
    :param patient: User input
    """
    db_patient = crud.get_patient_by_dni(
        db=db, dni=patient.dni
    )
    if db_patient:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="DNI already registered"
        )
    return crud.create_patient(
        db=db, patient=patient
    )

# Patient router operation for get all patients
@patients_router.get(
    "/",
    response_model=list[schemas.Patient],
    summary="Get all patients from database",
    include_in_schema=True,
)
def read_all_patients(
    skip: int = 0,
    limit: int = 1000000000,
    db: Session = Depends(get_db),
):
    """
    Get all patients with all information
    \f
    :param skip: min bound for patients id
    :param limit: max bound for patients id
    """
    patients = crud.get_all_patients(
        db=db, skip=skip, limit=limit
    )
    return patients

# Patient router operation for get a patient
# by its id
@patients_router.get(
    "/{patient_id}",
    response_model=schemas.Patient,
    summary="",
    include_in_schema=True,
)
def read_patient_by_id(
    patient_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a certain patient with all information by its id number

    - **patient_id**: the id of the patient to get
    \f
    :param patient_id: path parameter of type int
    """
    db_patient = crud.get_patient_by_id(
        db=db, patient_id=patient_id
    )
    return db_patient

"""Section for path operations router with anamnesis"""

# For create the ananemsis inform for a certain patient
@anamnesis_router.post(
    "/patient/{patient_id}",
    response_model=schemas.Anamnesis,
    summary="Create the anamensis inform for a certain patient",
    include_in_schema=True,
)
def create_anamnesis_for_patient(
    patient_id: int,
    anamnesis: schemas.AnamnesisCreate,
    db: Session = Depends(get_db),
):
    """
    Create Anamnesis inform for a certain patient

    - **description**: Here goes the inform description
    - **patient_id**: this parameter relates
    tables `patients` and `anamnesis` in the
    postgressql database and represents the id of
    the patient to set the anamnesis inform
    \f
    :param patient_id: path parameter of type int
    """
    return crud.create_patient_anamnesis(
        db=db,
        anamnesis=anamnesis,
        patient_id=patient_id
    )

# For get all the anamnesis informs of all patients
@anamnesis_router.get(
    "/",
    response_model=list[schemas.Anamnesis],
    summary="Get all the anamnesis informs of all patients",
    include_in_schema=True,
)
def read_anamnesis(
    skip: int = 0,
    limit: int = 1000000000000,
    db: Session = Depends(get_db),
):
    """
    Get a list of all anamnesis informs of all patients in the database
    \f
    :param skip: min bound for patients anamnesis id
    :param limit: max bound for patients anamnesis id
    """
    anamnesis_informs = crud.get_all_anamnesis(
        db=db, skip=skip, limit=limit
    )
    return anamnesis_informs

"""Section for path operations router with urgency informs"""

# For create the urgency inform for a certain patient
@urgency_informs_router.post(
    "/patient/{patient_id}",
    response_model=schemas.UrgencyInform,
    summary="Create the urgency inform for a certain patient",
    include_in_schema=True,
)
def create_urgency_inform_for_patient(
    patient_id: int,
    urgency_inform: schemas.UrgencyInformCreate,
    db: Session = Depends(get_db),
):
    """
    Create Urgency inform for a certain patient

    - **description**: Here goes the inform description
    - **patient_id**: this parameter relates
    tables `patients` and `urgency_inform` in the
    postgressql database and represents the id of
    the patient to set the urgency inform
    \f
    :param patient_id: path parameter of type int
    """
    return crud.create_patient_urgency_inform(
        db=db,
        urgency_inform=urgency_inform,
        patient_id=patient_id
    )

# For get all the urgency informs of all patients
@urgency_informs_router.get(
    "/",
    response_model=list[schemas.UrgencyInform],
    summary="Get all the urgency informs of all patients",
    include_in_schema=True,
)
def read_urgency_informs(
    skip: int = 0,
    limit: int = 1000000000000,
    db: Session = Depends(get_db),
):
    """
    Get a list of all urgency informs of all patients in the database
    \f
    :param skip: min bound for patients urgency informs id
    :param limit: max bound for patients urgency informs id
    """
    urgency_informs = crud.get_all_urgency_informs(
        db=db, skip=skip, limit=limit
    )
    return urgency_informs

# including routers
# including routing for pacients operations
app.include_router(patients_router)
app.include_router(anamnesis_router)
app.include_router(urgency_informs_router)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )