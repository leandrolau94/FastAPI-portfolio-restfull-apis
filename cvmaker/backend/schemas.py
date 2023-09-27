from pydantic import BaseModel

# For ProfessionalExperience model
class ProfessionalExperienceBase(BaseModel):
    place_of_work: str
    description: str
    duration_in_years: int

class ProfessionalExperienceCreate(ProfessionalExperienceBase):
    pass

class ProfessionalExperience(ProfessionalExperienceBase):
    id: int
    person_id: int

    class Config:
        orm_mode = True

# For Skills model
class SkillsBase(BaseModel):
    role: str
    description: str

class SkillsCreate(SkillsBase):
    pass

class Skills(SkillsBase):
    id: int
    person_id: int

    class Config:
        orm_mode = True

# For Projects model
class ProjectsBase(BaseModel):
    title: str
    description: str

class ProjectsCreate(ProjectsBase):
    pass

class Projects(ProjectsBase):
    id: int
    person_id: int

    class Config:
        orm_mode = True

# For Languages model
class LanguagesBase(BaseModel):
    name: str
    level: str

class LanguagesCreate(LanguagesBase):
    pass

class Languages(LanguagesBase):
    id: int
    person_id: int

    class Config:
        orm_mode = True

# For Person model
class PersonBase(BaseModel):
    full_name: str
    email: str
    address: str
    postal_code: int
    phone_number: str

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int
    work_experience: list[ProfessionalExperience] = []
    cv_skills: list[Skills] = []
    cv_projects: list[Projects] = []
    cv_languages: list[Languages] = []

    class Config:
        orm_mode = True