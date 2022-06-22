from sqlalchemy import Column, Integer, String, Numeric, Boolean, DateTime
from .Base import Base
class Project(Base):
    """
    Class responsible for managing department data:
    https://apis.e-conomic.com/#tag/Projects/operation/GetPageOfProjects
    """
    __tablename__ = 'projects'
    number = Column(Integer, primary_key=True)
    name = Column(String(255))
    project_group_number = Column(Integer)
    closed_date = Column(DateTime)
    contact_person_id = Column(Integer)
    cost_price = Column(Numeric(10,2))
    customer_number = Column(Integer)
    delivery_date = Column(DateTime)
    delivery_location_number = Column(Integer)
    department_number = Column(Integer)
    description = Column(String(255))
    fixed_price = Column(Numeric(10,2))
    invoiced_total = Column(Numeric(10,2))
    is_barred = Column(Boolean)
    is_closed = Column(Boolean)
    is_main_project = Column(Boolean)
    is_mileage_invoiced = Column(Boolean)
    last_updated = Column(DateTime)
    main_project_number = Column(Integer)
    mileage = Column(Numeric(10,2))
    object_version = Column(String(255))
    other_responsible_employeeNumber = Column(String(255))
    responsible_employee_number = Column(String(255))
    sales_price = Column(Numeric(10,2))
    status = Column(Integer)