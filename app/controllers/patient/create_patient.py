from app.models import Patient
from sqlalchemy.orm import Session
from app.views import NewPatient, NewPatientResponse
from datetime import date

async def createPatient(newPatient: NewPatient, session: Session) -> NewPatientResponse:
    try:
        patient = Patient(patient_name = newPatient.patient_name, phone_number= newPatient.phone_number, address= newPatient.address, gender = newPatient.gender, visit=date.today())
        session.add(patient)
        session.flush()
        session.commit()
        return NewPatientResponse(patient_name = newPatient.patient_name, phone_number= newPatient.phone_number, address= newPatient.address, gender = newPatient.gender, visit=date.today())
    except Exception as e:
        print(e)
        session.rollback()
        return None