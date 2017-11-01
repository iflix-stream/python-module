from sqlalchemy import Column,ForeignKey
from sqlalchemy.dialects.mysql import TINYINT,VARCHAR,TEXT,INTEGER
from base import Base

class Filme(Base):

    __tablename__ = "filme"

    id = Column(INTEGER, primary_key=True)
    nome = Column(VARCHAR(255), nullable=False)
    classificacao = Column(INTEGER(11), nullable=False)
    caminho = Column(VARCHAR(45), nullable=False)
    duracao = Column(VARCHAR(45), nullable=False)
    sinopse = Column(TEXT, nullable=False)
    thumbnail = Column(VARCHAR(255), nullable=False)
    genero_id = Column(INTEGER, ForeignKey('genero.id'), nullable=False)
    status = Column(TINYINT(4), nullable=False,default=1)


    def __init__(self,nome,classificacao,caminho,duracao,sinopse,thumbnail,genero_id):
        self.nome = nome
        self.classificacao = classificacao
        self.caminho = caminho
        self.duracao = duracao
        self.sinopse = sinopse
        self.thumbnail = thumbnail
        self.genero_id = genero_id


