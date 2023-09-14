from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer, index=True)
    genre = Column(String, index=True)
    country = Column(String, index=True)
    role = Column(String, index=True)
    wage = Column(Float, index=True)
    start_date = Column(DateTime, index=True)