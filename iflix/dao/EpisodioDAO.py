import collections

from iflix.models.Episodio import Episodio
from iflix.models.banco import bd


class EpisodioDAO:
    def retreave(self, args):
        session = bd()
        a = [{}]
        for id, nome, sinopse, temporada, duracao, caminho, serie, numero in session.query(Episodio.id, Episodio.nome,
                                                                                           Episodio.sinopse,
                                                                                           Episodio.temporada_id,
                                                                                           Episodio.duracao,
                                                                                           Episodio.caminho,
                                                                                           Episodio.serie_id,
                                                                                           Episodio.numero):
            a.append(
                {'id': id, 'nome': nome, 'sinopse': sinopse, 'temporada': temporada, 'duracao': caminho, 'serie': serie,
                 'numero': numero})
        a.pop(0)
        return a

    def create(self, result):
        session = bd()
        episodio = Episodio(
            nome=result['nome'], genero_id=result['sinopse'], caminho=result['temporada'],
            classificacao=result['duracao'], duracao=result['caminho'],
            sinopse=result['serie'], thumbnail=result['numero']
        )
        session.add(episodio)
        session.commit()

    def update(self, result):
        session = bd()
        episodio = session.query(Episodio).get(result['id'])
        if 'nome' in result:
            episodio.nome = result['nome']
        if 'sinopse' in result:
            episodio.sinopse = result['sinopse']
        if 'temporada' in result:
            episodio.temporada_id = result['temporada']
        if 'duracao' in result:
            episodio.duracao = result['duracao']
        if 'caminho' in result:
            episodio.caminho = result['caminho']
        if 'serie' in result:
            episodio.serie_id = result['serie']
        if 'numero' in result:
            episodio.numero = result['numero']
        session.commit()

    def delete(self, arg):
        session = bd()
        episodio = session.query(Episodio).get(arg)
        session.delete(episodio)
        session.commit()
