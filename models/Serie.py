from sqlalchemy import Column,ForeignKey
from sqlalchemy.dialects.mysql import TINYINT,VARCHAR,TEXT,INTEGER
from sqlalchemy.orm import relationship

from base import Base
from Genero import Genero
class Serie(Base):

    __tablename__ = "serie"

    id = Column(INTEGER, primary_key=True)
    nome = Column(VARCHAR(255), nullable=False)
    sinopse = Column(TEXT, nullable=False)
    classificacao = Column(INTEGER(11), nullable=False)
    thumbnail = Column(VARCHAR(255), nullable=False)
    genero_id = Column(INTEGER, ForeignKey('genero.id'), nullable=False)
    status = Column(TINYINT(4), nullable=False,default='1')
    genero = relationship(Genero,backref='serie_genero')


