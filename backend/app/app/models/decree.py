from email.policy import default

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship


from app.db.base_class import Base

if TYPE_CHECKING:
    from .decree_type import DecreeType
    from .decree_change_action import DecreeChangeAction



class Decree(Base):
    __tablename__ = "decree"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    mainId = Column(Integer)
    number = Column(String)
    date = Column(Date)
    isActive = Column(Integer, default=1)
    typeId = Column(Integer, ForeignKey('decree_type.id'))
    changeTypeId = Column(Integer, ForeignKey('decree_change_action.id'))

    type = relationship("DecreeType", backref="decree_type", viewonly=True)
    changeType = relationship("DecreeChangeAction", backref="decree_change_action", viewonly=True)
