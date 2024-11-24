from app.models import Patient
from sqlalchemy.orm import Session
from app.views import PatientSearch, PatientSearchResponse


async def getAllPatients(session: Session) -> list:
    return session.query(Patient).all()

#Retrieve patient by MRN not id?
async def getPatientByMRN(patientId: int, session: Session) -> PatientSearchResponse:
    patient = session.query(Patient).filter(Patient.MRN == patientId).first()
    if patient is None:
        return None
    return PatientSearchResponse(patient_name= patient.patient_name, MRN=patient.MRN, phone_number= patient.phone_number, address= patient.address, gender= patient.gender, visit= patient.visit, id= patient._id)
    
