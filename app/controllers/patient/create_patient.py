from app.models import Patient
from sqlalchemy.orm import Session
from app.views import NewPatient, NewPatientResponse
from datetime import date
import uuid

async def createPatient(newPatient: NewPatient, session: Session) -> NewPatientResponse:
    try:
        
        patient = Patient(
            patient_name = newPatient.patient_name, 
            phone_number= newPatient.phone_number, 
            address= newPatient.address, 
            gender = newPatient.gender,
            MRN=int(str(uuid.uuid4().int)[:10]),
            visit=date.today()
            )
        session.add(patient)
        session.commit()
        return NewPatientResponse(
            patient_name = newPatient.patient_name, 
            phone_number= newPatient.phone_number, 
            address= newPatient.address, 
            gender = newPatient.gender,
            visit=date.today(),
            message= 'Patient Created Successfully' #The error was from this field. It was missing !
            )
    except Exception as e:
        print(e.__str__())
        session.rollback()
        return None