from fastapi import APIRouter, HTTPException
from app.views import PatientSearch, PatientSearchResponse, NewPatient, NewPatientResponse
from app.controllers import getAllPatients, getPatientByMRN, deletePatientByMRN, createPatient
from app.config import session
from datetime import date
prouter = APIRouter()
@prouter.get("/patient/{MRN}")
async def read_patient(MRN: int)-> PatientSearchResponse:
    patient = await getPatientByMRN(MRN,session)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
@prouter.get("/patients")
async def read_patients():
    return await getAllPatients(session)

@prouter.delete("/patient/{MRN}")
async def delete_patient(MRN: int):
    patient = await getPatientByMRN(MRN,session)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    await deletePatientByMRN(MRN,session)
    return {"message": "Patient deleted successfully"}

@prouter.post("/patient")
async def create_patient(patient: NewPatient):
    newpatient = await createPatient(patient, session)
    if newpatient is None:
        raise HTTPException(status_code=500, detail= {'message':"failed to create patient"})
    
    return NewPatientResponse(patient_name=newpatient.patient_name, phone_number=newpatient.phone_number, address=newpatient.address, gender = newpatient.gender, visit=newpatient.visit, message="Patient successfully created")
   
