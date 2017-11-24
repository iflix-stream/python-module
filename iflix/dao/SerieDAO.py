import collections

from iflix.dao.ModeloDAO import ModeloDAO
from iflix.models.Filme import Filme
from iflix.models.Genero import Genero
from iflix.models.Serie import Serie
from iflix.models.banco import bd


class SerieDAO:
    def retreave(self, args):
        a = ModeloDAO().retreave(
            args=[Serie.id.name, Serie.nome.name, Serie.classificacao.name, Serie.sinopse.name, Serie.thumbnail.name,
                  Serie.genero_id.name], params=args, obj=Serie)
        session = bd()
        for i in a:
            classe = session.query(Genero).get(a[i][Serie.genero_id.name])
            a[i]['genero_nome'] = classe.nome
        return a

    def create(self, result):
        session = bd()
        serie = Serie(
            nome=result['nome'], genero_id=result['genero'], caminho=result['caminho'],
            classificacao=result['classificacao'], sinopse=result['sinopse'], thumbnail=result['thumbnail']
        )
        session.add(serie)
        session.commit()

    def update(self, result):
        session = bd()
        serie = session.query(Serie).get(result['id'])
        if 'classificacao' in result:
            serie.classificacao = result['classificacao']
        if 'sinopse' in result:
            serie.sinopse = result['sinopse']
        if 'caminho' in result:
            serie.caminho = result['caminho']
        if 'genero' in result:
            serie.genero_id = result['genero']
        if 'nome' in result:
            serie.nome = result['nome']
        if 'thumbnail' in result:
            serie.thumbnail = result['thumbnail']
        session.commit()

    def delete(self, arg):
        session = bd()
        serie = session.query(Serie).get(arg)
        session.delete(serie)
        session.commit()
