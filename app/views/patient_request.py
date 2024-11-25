from pydantic import BaseModel, Field, field_validator
from typing import Optional
 
class PatientSearch(BaseModel):
    MRN: int = Field(..., title='medical record number', description='patient MRN to identify patient', examples=[123])

class NewPatient(BaseModel):
    patient_name: str = Field(..., title='patient name', description='patient name', examples=['John Doe'])
    phone_number: str = Field(..., title='phone number', description='patient phone number', examples=['1234567890'])
    address: str = Field(..., title='address', description='patient address',  examples=['123 Main St'])
    gender: str = Field(..., title='gender', description = 'patient gender', examples=['M'], max_length=1)

class UpdatePatientRequest(BaseModel):
    MRN: int = Field(..., title='medical record number', description='patient MRN to identify patient', examples=[123])
    patient_name: Optional[str] = Field(None, title='Patient Name', description='Patient name', examples=['John Doe'])
    phone_number: Optional[str] = Field(None, title='Phone Number', description='Patient phone number', examples=['1234567890'])
    address: Optional[str] = Field(None, title='Address', description='Patient address', examples=['123 Main St'])
    gender: Optional[str] = Field(None, title='Gender', description='Patient gender', examples=['M'], max_length=1)