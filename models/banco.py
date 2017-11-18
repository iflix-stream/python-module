from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def bd():
    e = create_engine("mysql+pymysql://root:@10.1.6.23/bd_iflix")
    Session = sessionmaker()
    Session.configure(bind=e)
    return Session()