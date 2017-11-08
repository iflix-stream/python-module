from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def bd():
    e = create_engine("mysql+pymysql://root:@192.168.1.3/bd_iflix")
    Session = sessionmaker()
    Session.configure(bind=e)
    return Session()