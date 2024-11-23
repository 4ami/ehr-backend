from sqlalchemy import Column, Integer, String, Enum
from .base import Base
import enum



class Role(enum.Enum):
    RECEPTIONIST = 'RECEPTIONIST'
    PHARMACIST = 'PHARMACIST'
    CASHIER = 'CASHIER'

class User(Base):
    __tablename__ = 'user'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(String(35), nullable=False)
    full_name = Column(String(70), nullable=False)
    role = Column(Enum(Role), nullable=False)
    password = Column(String(257), nullable=False)
