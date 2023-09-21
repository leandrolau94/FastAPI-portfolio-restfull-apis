from pydantic import BaseModel
from datetime import datetime

class EmployeeBase(BaseModel):
    full_name: str
    email: str
    age: int
    genre: str
    country: str
    role: str
    wage: float
    start_date: datetime = datetime.now()

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True