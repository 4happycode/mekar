from pydantic import BaseModel, validator
from datetime import date
import re


# Skema Pydantic untuk data masukan
class FormDataCreate(BaseModel):
    name: str
    identityNumber: int
    email: str
    dateOfBirth: date
    
    @validator('name')
    def name_alphabetical(cls, v):
        if not v.isalpha():
            raise ValueError('Name must only contain alphabetical characters')
        return v

    @validator('identityNumber')
    def identity_number_numeric(cls, v):
        if not str(v).isdigit():
            raise ValueError('Identity number must only contain numeric characters')
        return v
    
    @validator('email')
    def email_format(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError('Email must be a valid email address')
        return v
    
    @validator('dateOfBirth')
    def date_format(cls, v):
        if not isinstance(v, date):
            raise ValueError('Must be a valid date')
        return v

# Skema Pydantic untuk data keluaran
class FormData(BaseModel):
    id: int
    name: str
    identity_number: int
    email: str
    date_of_birth: date

    class Config:
        orm_mode = True
