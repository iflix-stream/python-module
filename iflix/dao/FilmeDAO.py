from iflix.dao.ModeloDAO import ModeloDAO
from iflix.models.Filme import Filme
from iflix.models.banco import bd


class FilmeDAO:
    def retreave(self,args):
        return ModeloDAO().retreave(args=[Filme.id.name,Filme.nome.name],params={},obj=Filme)
    def create(self,result):
        session = bd()
        filme = Filme(
            nome=result['nome'], genero_id=result['genero'], caminho=result['caminho'],
            classificacao=result['classificacao'], duracao=result['duracao'],
            sinopse=result['sinopse'], thumbnail=result['thumbnail']
        )
        session.add(filme)
        session.commit()
    def update(self,result):
        session = bd()
        filme = session.query(Filme).get(result['id'])
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
    def delete(self,arg):
        session = bd()
        filme = session.query(Filme).get(arg)
        session.delete(filme)
        session.commit()