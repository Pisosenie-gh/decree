from email.policy import default

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, ARRAY
from sqlalchemy.orm import relationship


from app.db.base_class import Base

if TYPE_CHECKING:
    from .eds_provider_type import EdsProviderType
    from .signature import Signature



class Eds(Base):
    __tablename__ = "eds"

    id = Column(Integer, primary_key=True, index=True)
    signDate = Column(DateTime)
    certStartDate = Column(DateTime)
    certEndDate = Column(DateTime)
    certOwner = Column(String)
    PUID = Column(String)
    cert = Column(String)
    content = Column(String)
    signedFilesIdSequence = Column(ARRAY(Integer))
    signedFieldsSequence = Column(ARRAY(String))
    



    providerTypeId = Column(Integer, ForeignKey('eds_provider_type.id'), nullable=True)
    signatureId = Column(Integer, ForeignKey('signature.id'), nullable=True)

    providerType = relationship("EdsProviderType", backref="init")
    signature = relationship("Signature", backref="signature", viewonly=True, foreign_keys='Eds.signatureId')