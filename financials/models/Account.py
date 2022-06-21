from sqlalchemy import Column, Integer, String, Numeric
from .Base import Base
class Account(Base):
    __tablename__ = 'accounts'
    account_number = Column(Integer, primary_key=True)
    account_type = Column(String(255))
    balance = Column(Numeric(10,2))
    block_direct_entries = Column(String(255))
    debit_credit = Column(String(255))
    name = Column(String(255))
