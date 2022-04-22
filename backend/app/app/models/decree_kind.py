from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String


from app.db.base_class import Base



class DecreeKind(Base):
    __tablename__ = "decree_kind"

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(String)
    nameKz = Column(String)
