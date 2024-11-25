from sqlalchemy.orm import Session
from app.models import Patient
from app.views import UpdatedPateintResponse, UpdatePatientRequest
async def update(request: UpdatePatientRequest, session:Session) -> UpdatedPateintResponse:
    patient = session.query(Patient).filter(Patient.MRN == request.MRN).first()
    
    if patient is None: return None

    old = {}
    old['patient_name'] = patient.patient_name
    old['phone_number'] = patient.phone_number
    old['address'] = patient.address
    old['gender'] = patient.gender

    patient.patient_name = request.patient_name if request.patient_name is not None else patient.patient_name
    patient.phone_number = request.phone_number if request.phone_number is not None else patient.phone_number
    patient.address = request.address if request.address is not None else patient.address
    patient.gender = request.gender if request.gender is not None else patient.gender
    session.commit()
    return UpdatedPateintResponse(
        patient_name_old=old['patient_name'],
        patient_name_new=patient.patient_name,
        phone_number_old=old['phone_number'],
        phone_number_new=patient.phone_number,
        address_old=old['address'],
        address_new=patient.address,
        gender_old=old['gender'],
        gender_new=patient.gender
    )
