from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
def bd():
    e = create_engine("mysql+pymysql://root:@localhost/bd_iflix")
    Session = sessionmaker()
    Session.configure(bind=e)
    return Session()