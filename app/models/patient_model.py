from .base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey

class Patient(Base):
    __tablename__ = 'patient'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    patient_name = Column(String(35), nullable=False)
    MRN = Column(Integer, nullable=True, autoincrement=True)
    phone_number = Column(String(10), nullable=False)
    address = Column(String(70), nullable=False)
    visit = Column(Date, nullable=False)
    gender = Column(String(1), nullable=False)
