from email.policy import default

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from app.db.base_class import Base

if TYPE_CHECKING:
    from .replacement_type import ReplacementType



class Replaced(Base):
    __tablename__ = "signature_replaced"

    id = Column(Integer, primary_key=True, index=True)
    employeeId = Column(Integer)
    fullNameRu = Column(String)
    fullNameKz = Column(String)
    positionRu = Column(String)
    positionKz = Column(String)
    departmentRu = Column(String)
    departmentKz = Column(String)

    replacementTypeId = Column(Integer, ForeignKey('replacement_type.id'), nullable=True)

    replacementType = relationship("ReplacementType", backref="init")

