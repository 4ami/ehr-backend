from sqlalchemy import Integer, Column, String
from .base import Base

class DepartmentModel(Base):
    __tablename__ = 'department'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(50), nullable=False)