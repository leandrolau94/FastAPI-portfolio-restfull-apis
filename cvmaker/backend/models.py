from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from phonenumbers.phonenumber import PhoneNumber
from sqlalchemy.orm import relationship

from .database import Base

class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String, index=True)
    postal_code = Column(Integer, index=True)
    phone_number = Column(PhoneNumber, index=True)

    work_experience = relationship(
        "ProfessionalExperience",
        back_populates="person"
    )
    cv_skills = relationship(
        "Skills",
        back_populates="person"
    )
    cv_projects = relationship(
        "Projects",
        back_populates="person"
    )
    cv_languages = relationship(
        "Languages",
        back_populates="person"
    )

class ProfessionalExperience(Base):
    __tablename__ = "professional_experiences"

    id = Column(Integer, primary_key=True, index=True)
    place_of_work = Column(String, index=True)
    description = Column(String, index=True)
    duration_in_years = Column(Integer, index=True)
    person_id = Column(Integer, ForeignKey("people.id"))

    person = relationship(
        "Person",
        back_populates="work_experience"
    )

class Skills(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, index=True)
    description = Column(String, index=True)
    person_id = Column(Integer, ForeignKey("people.id"))

    person = relationship(
        "Person",
        back_populates="cv_skills"
    )

class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Integer, index=True)
    description = Column(String, index=True)
    person_id = Column(Integer, ForeignKey=("people.id"))

    person = relationship(
        "Person",
        back_populates="cv_projects"
    )

class Languages(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String, index=True)
    person_id = Column(Integer, ForeignKey=("people.id"))

    person = relationship(
        "Person",
        back_populates="cv_languages"
    )