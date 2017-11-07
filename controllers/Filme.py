import json
import itertools

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Filme import Filme
from marshmallow import fields


class FilmeResource:
    def on_get(self, req, resp):
        e = create_engine("mysql+pymysql://root:root@localhost/test")
        Session = sessionmaker()
        Session.configure(bind=e)
        session = Session()
        i={}
        o=0
        for id,nome,genero,caminho,classificacao,duracao in session.query(Filme.id,Filme.nome,Filme.genero,Filme.caminho,Filme.classificacao,Filme.duracao)[1:3]:
            i[o]={

                'id':id,
                'nome':nome,
                'genero':{
                    'id':genero,
                    'nome':genero
                },
                'caminho':caminho
            }
            o=o+1
        resp.body = json.dumps(i)
        resp.set_header('Content-Type', 'application/json')
        resp.content_type = "application/json"