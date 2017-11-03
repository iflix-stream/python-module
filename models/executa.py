from sqlalchemy import create_engine

import base

import Filme
import Genero

from sqlalchemy.orm import sessionmaker

e = create_engine("mysql+pymysql://root:root@localhost/test")
session = sessionmaker()
session.configure(bind=e)
base.Base.metadata.create_all(e,checkfirst=True)
g = Genero.Genero(nome='asd')
f = Filme.Filme(nome = 'asdsda',classificacao='123',caminho='dsad',duracao='1:50',sinopse='sdasd',thumbnail='asdsd',genero = g)
s = session()
s.add(g)
s.add(f)
s.commit()
s.commit()