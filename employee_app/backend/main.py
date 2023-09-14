from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# setting up cors policy
origins = [
    "http://0.0.0.0:8000",
    "http://localhost:3000",
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

# Endpoints Definition for consuming them in the frontend
endpoints = {
    "create_new_employee": "/employees/",
    "read_all_employes": "/employees/",
}

# endpoint for create a new employee
@app.post(
    endpoints["create_new_employee"],
    response_model=schemas.Employee,
    summary="Create a new employee in the database",
    include_in_schema=True,
)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new employee in the database along with its requires information

    - **`full_name`**: The employee's name
    - **`email`**: The employee's email contact
    - **`age`**: The employee's age
    - **`genre`**: The employee's genre
    - **`country`**: The employee country
    - **`role`**: The employee role
    - **`wage`**: The employee wage
    - **`start_date`**: The employee started date
    """
    db_employee = crud.get_employee_by_email(
        db=db, email=employee.email
    )
    if db_employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee email already registered"
        )
    return crud.create_employee(
        db=db, employee=employee
    )

# endpoint for read all employees
@app.get(
    endpoints["read_all_employes"],
    response_model=list[schemas.Employee],
    summary="Read all employees from the database along with its required information",
    include_in_schema=True,
)
def read_all_employees(
    skip: int = 0,
    limit: int = 10000,
    db: Session = Depends(get_db),
):
    employees = crud.read_all_employees(
        db=db, skip=skip, limit=limit
    )
    return employees

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )