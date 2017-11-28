from passlib.hash import bcrypt, bcrypt_sha256
from iflix.dao.ModeloDAO import ModeloDAO
from iflix.models.Temporada import Temporada
from iflix.models.Usuario import Usuario
from iflix.models.banco import bd


class TemporadaDAO:
    def retreave(self, args):
        session = bd()
        a = [{}]
        for instance in session.query(Temporada).order_by(Temporada.id):
            a.append({'id':instance.id,'numero':instance.numero,'serie':instance.serie_id})
        a.pop(0)
        return a

    def create(self, result):
        session = bd()
        temporada = Temporada(numero=result['numero'], serie_id=result['serie'])
        session.add(temporada)
        session.commit()

    def update(self, result):
        session = bd()
        temporada = session.query(Temporada).get(result['id'])
        if 'numero' in result:
            temporada.numero = result['numero']
        if 'serie' in result:
            temporada.serie_id = result['serie']
        session.commit()

    def delete(self, arg):
        session = bd()
        temporada = session.query(Temporada).get(arg)
        session.delete(temporada)
        session.commit()
