from pydantic import BaseModel

# For Anamnesis
class AnamnesisBase(BaseModel):
    description: str | None = None

class AnamnesisCreate(AnamnesisBase):
    pass

class Anamnesis(AnamnesisBase):
    id: int
    patient_id: int

    class Config:
        # for replacing the orm_mode = True
        from_attributes = True

# For UrgencyInform
class UrgencyInformBase(BaseModel):
    description: str | None = None

class UrgencyInformCreate(UrgencyInformBase):
    pass

class UrgencyInform(UrgencyInformBase):
    id: int
    patient_id: int

    class Config:
        # for replacing the orm_mode = True
        from_attributes = True

# For CronologicEvolution
class CronologicEvolutionBase(BaseModel):
    description: str | None = None

class CronologicEvolutionCreate(CronologicEvolutionBase):
    pass

class CronologicEvolution(CronologicEvolutionBase):
    id: int
    patient_id: int

    class Config:
        # for replacing the orm_mode = True
        from_attributes = True

# For MedicalOrders
class MedicalOrdersBase(BaseModel):
    description: str | None = None

class MedicalOrdersCreate(MedicalOrdersBase):
    pass

class MedicalOrders(MedicalOrdersBase):
    id: int
    patient_id: int

    class Config:
        # for replacing the orm_mode = True
        from_attributes = True

# For Pacient
class PatientBase(BaseModel):
    full_name: str
    email: str
    genre: str
    age: int
    address: str
    dni: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    anamnesis: list[Anamnesis] = []
    urgency_inform: list[UrgencyInform] = []
    cronologic_evolution: list[CronologicEvolution] = []
    medical_orders: list[MedicalOrders] = []

    class Config:
        # for replacing the orm_mode = True
        from_attributes = True