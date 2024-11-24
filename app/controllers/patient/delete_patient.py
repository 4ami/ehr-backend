from app.models import Patient
from sqlalchemy.orm import Session

async def deletePatientByMRN(patientId: int, session: Session) -> bool:
    patient = session.query(Patient).filter(Patient.MRN == patientId).first()
    if patient is None:
        return False
    session.delete(patient)
    session.commit()
    return True