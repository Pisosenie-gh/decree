from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String


from app.db.base_class import Base



class Signer(Base):
    __tablename__ = "signer"

    id = Column(Integer, primary_key=True, index=True)
    employeeId = Column(Integer)
    fullNameRu = Column(String)
    fullNameKz = Column(String)
    positionRu = Column(String)
    positionKz = Column(String)
    departmentRu = Column(String)
    departmentKz = Column(String)
