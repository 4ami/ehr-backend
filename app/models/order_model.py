from .base import Base
from sqlalchemy import Column, Integer, String, Enum
import enum

class OrderTypes(enum.Enum):
    CONSULTATION='CONSULTATION'
    LAB='LAB'
    IMAGING='IMAGING'
    MEDICATION='MEDICATION'

class OrderStatus(enum.Enum):
    PENDING='PENDING'
    PROCESSED='PROCESSED'
    REJECTED='REJECTED'

class OrderModel(Base):
    __tablename__ = 'order'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum(OrderTypes), nullable=False)
    status = Column(Enum(OrderStatus), nullable=False, default='PENDING')
    department = Column(Integer, nullable=True)
