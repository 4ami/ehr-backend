from .base import Base
from sqlalchemy import Column, Integer, BigInteger, String, Date, Sequence

class Patient(Base):
    __tablename__ = 'patient'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    patient_name = Column(String(35), nullable=False)
    MRN = Column(BigInteger, nullable=False, unique=True)
    phone_number = Column(String(10), nullable=False)
    address = Column(String(70), nullable=False)
    visit = Column(Date, nullable=False)
    gender = Column(String(1), nullable=False)
