from pydantic import BaseModel, Field
from datetime import date

class PatientSearchResponse(BaseModel):
    patient_name: str = Field(..., title='patient name', description='patient name')
    MRN: int = Field(..., title='medical record number', description='patient MRN to identify patient', examples=[123])
    phone_number: str = Field(..., title='phone number', description='patient phone number')
    address: str = Field(..., title='address', description='patient address')
    visit: date = Field(..., title='visit', description='patient visit date')
    id: int = Field(..., title='patient id', description='patient id')
    gender: str = Field(..., title='gender', description = 'patient gender')

class NewPatientResponse(BaseModel):
    patient_name: str = Field(..., title='patient name', description='patient name')
    phone_number: str = Field(..., title='phone number', description='patient phone number')
    address: str = Field(..., title='address', description='patient address')
    gender: str = Field(..., title= "gender", description = 'patient gender')
    visit: date = Field(..., title='visit', description='patient visit date')
    message: str = Field(..., title='message', description='Patient successfully created')