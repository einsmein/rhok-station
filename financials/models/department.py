from sqlalchemy import Column, Integer, String, Numeric
from .Base import Base
class Department(Base):
    """
    Class responsible for managing department data:
    https://restdocs.e-conomic.com/#departments
    """
    __tablename__ = 'departments'
    department_number = Column(Integer, primary_key=True)
    name = Column(String(255))
