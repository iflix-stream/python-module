import json

import falcon
from cerberus import Validator
from util.DecodeReq import parse
from models.Filme import Filme
from models.banco import bd


class FilmeResource:
    def on_get(self, req, resp):
        session = bd()
        i = {}
        o = 0
        for id, nome, genero, caminho, classificacao, duracao, sinopse, thumbnail in session.query(
                Filme.id, Filme.nome,
                Filme.genero_id,
                Filme.caminho,
                Filme.classificacao,
                Filme.duracao,
                Filme.sinopse,
                Filme.thumbnail):
            i[o] = {
                'id': id,
                'nome': nome,
                'classificacao': classificacao,
                'caminho': caminho,
                "duracao": duracao,
                "sinopse": sinopse,
                "thumbnail": thumbnail,
                "genero_id": genero
            }
            o = o + 1
        resp.body = json.dumps(i)
        resp.set_header('Content-Type', 'application/json')
        resp.content_type = "application/json"
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        session = bd()
        v = Validator()
        schema = {
            'nome': {
                'required': True
            },
            'genero': {
                'required': True
            },
            'caminho': {
                'required': True
            },
            'classificacao': {
                'required': True,
                'type': 'integer'
            },
            'duracao': {
                'required': True
            },
            'sinopse': {
                'required': True
            },
            'thumbnail': {
                'required': True
            }
        }
        result = parse(req)
        if (v.validate(result, schema)):
            filme = Filme(
                nome=result['nome'], genero_id=result['genero'], caminho=result['caminho'],
                classificacao=result['classificacao'], duracao=result['duracao'],
                sinopse=result['sinopse'], thumbnail=result['thumbnail']
            )
            session.add(filme)
            session.commit()
            resp.status = falcon.HTTP_CREATED
        else:
            resp.body = json.dumps(v.errors)
            resp.status = falcon.HTTP_400
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')

    def on_put(self, req, resp):
        result = parse(req)
        resp.status = falcon.HTTP_400
        if ('id' in req.params):
            session = bd()
            filme = session.query(Filme).get(req.params['id'])
            if ('classificacao' in result):
                filme.classificacao = result['classificacao']
            if ('sinopse' in result):
                filme.sinopse = result['sinopse']
            if ('caminho' in result):
                filme.caminho = result['caminho']
            if ('genero' in result):
                filme.genero_id = result['genero']
            if ('duracao' in result):
                filme.duracao = result['duracao']
            if ('nome' in result):
                filme.nome = result['nome']
            if ('thumbnail' in result):
                filme.thumbnail = result['thumbnail']
            session.commit()
            resp.status = falcon.HTTP_NO_CONTENT
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_400
        if ('id' in req.params):
            session = bd()
            filme = session.query(Filme).get(req.params['id'])
            session.delete(filme)
            session.commit()
            resp.status = falcon.HTTP_NO_CONTENT
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')
