from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(
        Integer, primary_key=True, index=True,
    )
    full_name = Column(
        String, index=True,
    )
    email = Column(
        String, unique=True, index=True,
    )
    genre = Column(
        String, index=True,
    )
    age = Column(
        Integer, index=True,
    )
    address = Column(
        String, index=True,
    )
    dni = Column(
        String, unique=True, index=True,
    )

    anamnesis = relationship(
        "Anamnesis",
        back_populates="patient",
    )
    urgency_inform = relationship(
        "UrgencyInform",
        back_populates="patient",
    )
    cronologic_evolution = relationship(
        "CronologicEvolution",
        back_populates="patient",
    )
    medical_orders = relationship(
        "MedicalOrders",
        back_populates="patient"
    )

class Anamnesis(Base):
    __tablename__ = "anamnesis"

    id = Column(
        Integer, primary_key=True, index=True,
    )
    description = Column(
        Text, index=True,
    )
    pacient_id = Column(
        Integer,
        ForeignKey(
            "patients.id",
            ondelete='CASCADE',
        ),
    )

    patient = relationship(
        "Patient",
        back_populates="anamnesis",
    )

class UrgencyInform(Base):
    __tablename__ = "urgency_inform"

    id = Column(
        Integer, primary_key=True, index=True,
    )
    description = Column(
        Text, index=True,
    )
    pacient_id = Column(
        Integer,
        ForeignKey(
            "patients.id",
            ondelete='CASCADE',
        )
    )

    patient = relationship(
        "Patient",
        back_populates="urgency_inform"
    )

class CronologicEvolution(Base):
    __tablename__ = "cronologic_evolution"

    id = Column(
        Integer, primary_key=True, index=True,
    )
    description = Column(
        Text, index=True,
    )
    pacient_id = Column(
        Integer,
        ForeignKey(
            "patients.id",
            ondelete='CASCADE',
        )
    )

    patient = relationship(
        "Patient",
        back_populates="cronologic_evolution"
    )

class MedicalOrders(Base):
    __tablename__ = "medical_orders"

    id = Column(
        Integer, primary_key=True, index=True,
    )
    description = Column(
        Text, index=True,
    )
    pacient_id = Column(
        Integer,
        ForeignKey(
            "patients.id",
            ondelete='CASCADE',
        )
    )

    patient = relationship(
        "Patient",
        back_populates="medical_orders"
    )

# class ClinicalStory(Base):
#     __tablename__ = "clinical_story"

#     id = Column(
#         Integer, primary_key=True, index=True,
#     )
#     complementary_explorations = Column(
#         Text, index=True,
#     )
#     interquery_paper = Column(
#         Text, index=True,
#     )
#     surgical_consent = Column(
#         Boolean, index=True,
#     )
#     anesthesia_inform = Column(
#         Text, index=True,
#     )
#     operating_room_inform = Column(
#         Text, index=True,
#     )
#     pathology_report = Column(
#         Text, index=True,
#     )
#     nursing_care = Column(
#         Text, index=True,
#     )
#     nursing_therapeutic_application = Column(
#         Text, index=True,
#     )
#     discharge_clinical_report = Column(
#         Text, index=True,
#     )
#     mental_health_clinical_story = Column(
#         Text, index=True,
#     )
#     pediatric_medical_story = Column(
#         Text, index=True,
#     )
#     nutritional_medical_story = Column(
#         Text, index=True,
#     )
#     gynecology_obstetrics_story = Column(
#         Text, index=True,
#     )
#     traumatology_medical_story = Column(
#         Text, index=True,
#     )