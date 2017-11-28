import collections

from iflix.dao.ModeloDAO import ModeloDAO
from iflix.models.Episodio import Episodio
from iflix.models.Filme import Filme
from iflix.models.Genero import Genero
from iflix.models.Serie import Serie
from iflix.models.Temporada import Temporada
from iflix.models.banco import bd


class SerieDAO:
    def retreave(self, args):
        index = 1
        a = ModeloDAO().retreave(
            args=[Serie.id.name, Serie.nome.name, Serie.classificacao.name, Serie.sinopse.name, Serie.thumbnail.name,
                  Serie.genero_id.name], params=args, obj=Serie)
        session = bd()
        for i in a:
            indexTemp =1
            indexEp = 1
            a[index]['temporadas'] = [{}]
            for temp in session.query(Temporada).filter_by(serie_id=a[index][Serie.id.name]):
                dici = {}
                dici['id'] = temp.id
                a[index]['temporadas'].append(dici)
                a[index]['temporadas'][indexTemp]['episodios'] = [{}]
                for ep in session.query(Episodio).filter_by(temporada_id=temp.id):
                    a[index]['temporadas'][indexTemp]['episodios'].append({'id':ep.id})
                    indexEp += 1
                a[index]['temporadas'][indexTemp]['episodios'].pop(0)
                indexTemp += 1
        index += 1
        a[1]['temporadas'].pop(0)
        a.pop(0)
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
