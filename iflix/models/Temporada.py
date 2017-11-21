from sqlalchemy import Column,ForeignKey
from sqlalchemy.dialects.mysql import TINYINT,VARCHAR,TEXT,INTEGER
from sqlalchemy.orm import relationship

from base import Base
from Serie import Serie
class Temporada(Base):

    __tablename__ = "temporada"

    id = Column(INTEGER, primary_key=True)
    numero = Column(INTEGER, nullable=False)
    serie_id = Column(INTEGER,ForeignKey('serie.id'),nullable=False)
    serie = relationship(Serie,backref='temporada_serie')


