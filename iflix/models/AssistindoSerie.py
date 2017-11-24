from sqlalchemy import Column,ForeignKey
from sqlalchemy.dialects.mysql import TINYINT,VARCHAR,TEXT,INTEGER
from base import Base

class AssistindoSerie(Base):

    __tablename__ = "assistindo_serie"

    idassistindo_serie = Column(INTEGER, primary_key=True)
    episodio_id = Column(INTEGER(11), nullable=False)
    horario_play = Column(INTEGER(11), nullable=False)
    usuario_id = Column(INTEGER(11), nullable=False)

