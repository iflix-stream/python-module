from sqlalchemy import Column,ForeignKey
from sqlalchemy.dialects.mysql import TINYINT,VARCHAR,TEXT,INTEGER
from base import Base

class AssistindoFilme(Base):

    __tablename__ = "assistindo_filme"

    idassistindo_filme = Column(INTEGER, primary_key=True)
    filme_id = Column(INTEGER(11), nullable=False)
    horario_play = Column(INTEGER(11), nullable=False)
    usuario_id = Column(INTEGER(11), nullable=False)

