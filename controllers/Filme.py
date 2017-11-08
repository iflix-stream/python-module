import json

from models.Filme import Filme
from models.banco import bd

class FilmeResource:
    def on_get(self, req, resp):
        session = bd()
        i={}
        o=0
        for id,nome,genero,caminho,classificacao,duracao,sinopse,thumbnail in session.query(Filme.id,Filme.nome,Filme.genero_id,Filme.caminho,Filme.classificacao,Filme.duracao,Filme.sinopse,Filme.thumbnail):
            i[o]={
                'id':id,
                'nome':nome,
                'classificacao':classificacao,
                'caminho':caminho,
                "duracao":duracao,
                "sinopse":sinopse,
                "thumbnail":thumbnail,
                "genero_id":genero
            }
            o=o+1
        resp.body = json.dumps(i)
        resp.set_header('Content-Type', 'application/json')
        resp.content_type = "application/json"