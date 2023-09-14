from sqlalchemy.orm import Session
import models, schemas

# For create employee endpoint
def get_employee_by_email(
        db: Session,
        email: str,
):
    return db.query(models.Employee).filter(
        models.Employee.email == email
    ).first()

def create_employee(
        db: Session,
        employee: schemas.EmployeeCreate,
):
    db_employee = models.Employee(
        full_name=employee.full_name,
        email=employee.email,
        age=employee.age,
        genre=employee.genre,
        country=employee.country,
        role=employee.role,
        wage=employee.wage,
        start_date=employee.start_date
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# For read all employees endpoint
def read_all_employees(
        db: Session,
        skip: int = 0,
        limit: int = 10000,
):
    return db.query(models.Employee).offset(
        skip
    ).limit(limit).all()