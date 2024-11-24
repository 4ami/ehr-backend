from ..models import Patient
from ..config import session
from datetime import date

def seed_patients():
    print('Patient seeder running ...')

    patients = [
        Patient(
            patient_name='Angham mohammed',
            MRN=123456,  # Replace this with appropriate logic if MRN is auto-incremented
            phone_number='5551234567',
            address='123 Main St, Springfield',
            visit=date(2024, 11, 23),  # Example visit date
            gender='F'
        )
    ]

    session.add_all(patients)
    session.commit()
    print('Patient seeder success ...')
