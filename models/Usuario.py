from sqlalchemy import Column,ForeignKey
from sqlalchemy.dialects.mysql import TINYINT,VARCHAR,TEXT,INTEGER,DATE
from sqlalchemy.orm import relationship

from base import Base
class Usuario(Base):

    __tablename__ = "usuario"

    id = Column(INTEGER, primary_key=True)
    nome = Column(VARCHAR(180), nullable=False)
    avatar = Column(VARCHAR(100), nullable=False)
    isControleDosPais = Column(TINYINT(4), nullable=False,default=0)
    senha = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False)
    dataNascimento = Column(DATE, nullable=False)
    dataCriacao = Column(DATE, nullable=False)
    dataAlteracao = Column(DATE, nullable=False)
    status = Column(TINYINT(4), nullable=False,default=1)
    isOnline = Column(TINYINT(4), nullable=False,default=0)


