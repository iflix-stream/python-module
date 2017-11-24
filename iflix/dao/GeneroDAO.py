
from iflix.dao.ModeloDAO import ModeloDAO
from iflix.models.Genero import Genero
from iflix.models.banco import bd


class GeneroDAO:
    def retreave(self, args):
        return ModeloDAO().retreave(args=[Genero.id.name,Genero.nome.name],params=args,obj=Genero)

    def create(self, result):
        session = bd()
        genero = Genero(nome=result['nome'])
        session.add(genero)
        session.commit()

    def update(self, result):
        session = bd()
        genero = session.query(Genero).get(result['id'])
        if 'nome' in result:
            genero.nome = result['nome']
        session.commit()

    def delete(self, arg):
        session = bd()
        genero = session.query(Genero).get(arg)
        session.delete(genero)
        session.commit()
