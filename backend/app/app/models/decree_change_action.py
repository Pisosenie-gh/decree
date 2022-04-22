from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String


from app.db.base_class import Base



class DecreeChangeAction(Base):
    __tablename__ = "decree_change_action"

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(String)
    nameKz = Column(String)
