from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import Filme
import Genero
import base

e = create_engine("mysql+pymysql://root@192.168.1.3/test")
session = sessionmaker()
session.configure(bind=e)
base.Base.metadata.create_all(e, checkfirst=True)
