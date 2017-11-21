from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import Filme
import Genero
import base

e = create_engine("mysql+pymysql://root@192.168.1.3/test")
session = sessionmaker()
session.configure(bind=e)
base.Base.metadata.create_all(e, checkfirst=True)
g = Genero.Genero(nome='asd')
f = Filme.Filme(nome ='A mumia', classificacao='123', caminho='dsad', duracao='1:50', sinopse='sdasd', thumbnail='asdsd', genero = g)
s = session()
s.add(g)
s.add(f)
s.commit()
s.commit()