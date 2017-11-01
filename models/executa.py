from sqlalchemy import create_engine

import base

import Genero
import Filme

e = create_engine("mysql+pymysql://root:root@localhost/test", echo=True)
base.Base.metadata.create_all(e,checkfirst=True)
