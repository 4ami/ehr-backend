from pydantic import BaseModel, Field
 
class PatientSearch(BaseModel):
    MRN: int = Field(..., title='medical record number', description='patient MRN to identify patient', examples=[123])

class NewPatient(BaseModel):
    patient_name: str = Field(..., title='patient name', description='patient name', examples=['John Doe'])
    phone_number: str = Field(..., title='phone number', description='patient phone number', examples=['1234567890'])
    address: str = Field(..., title='address', description='patient address',  examples=['123 Main St'])
    gender: str = Field(..., title='gender', description = 'patient gender', examples=['M'], max_length=1)

