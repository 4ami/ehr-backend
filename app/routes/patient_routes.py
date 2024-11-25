from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.views import PatientSearchResponse, NewPatient, NewPatientResponse, UpdatePatientRequest, UpdatedPateintResponse
from app.controllers import getAllPatients, getPatientByMRN, deletePatientByMRN, createPatient, update
from app.config import session
from datetime import date

prouter = APIRouter()

@prouter.get("/patients", description='Retrieve all patients', name='Get all patients')
async def read_patients():
    return await getAllPatients(session)

@prouter.get("/patient/{MRN}", description='Find specific patient using Medical Number Record (MRN)', name='Search for patient using MRN')
async def read_patient(MRN: int)-> PatientSearchResponse:
    patient = await getPatientByMRN(MRN,session)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

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

        detail = NewPatientResponse(
            patient_name=patient.patient_name, 
            phone_number=patient.phone_number, 
            address=patient.address, 
            gender = patient.gender, 
            visit=date.today(),
            message="Failed To Create Patient"
            )
        
        raise HTTPException( status_code=500, detail= detail.__dictionary__() )
    
    return JSONResponse(
        content= NewPatientResponse(
        patient_name=newpatient.patient_name, 
        phone_number=newpatient.phone_number, 
        address=newpatient.address, 
        gender = newpatient.gender, 
        visit=newpatient.visit,
        message="Patient successfully created"
        ).__dictionary__(),
        status_code= 202,
        
    )
   
@prouter.put('/patient', name='Update Patient Using MRN')
async def updatePatient(request:UpdatePatientRequest) -> UpdatedPateintResponse:
    updated = await update(request=request, session=session)
    if updated is None:
        raise HTTPException(status_code=404, detail={'message': f'Invalid MRN: {request.MRN}'})
    return updated