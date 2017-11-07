from sqlalchemy import Column,ForeignKey
from sqlalchemy.dialects.mysql import TINYINT,VARCHAR,TEXT,INTEGER
from sqlalchemy.orm import relationship

from base import Base
from Genero import Genero
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
    genero = relationship(Genero,backref='filme_genero')

    def to_json(self):
        return dict(id=self.id,nome=self.nome,classificacao=self.classificacao,
                    caminho=self.caminho,duracao=self.duracao,sinopse=self.sinopse,
                    thumbnail=self.thumbnail,genero_id=self.genero_id)




