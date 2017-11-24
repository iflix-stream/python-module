from iflix.models.Filme import Filme
from iflix.models.Genero import Genero
from iflix.models.banco import bd
import collections


class ModeloDAO:
    def retreave(self, args, params, obj):
        # faltando arrumar  limite  para dps adicionar o resto das query nas funções
        if 'id' in params:
            return self.retreaveId(args, params, obj)
        elif 'genero' in params:
            return self.retreaveGenero(args, params, obj)
        elif 'nome' in params:
            return self.retreaveNome(args, params, obj)

        return self.retreaveAll(args, params, obj)

    def retreaveAll(self, args, params, obj):
        session = bd()
        i = collections.defaultdict(dict)
        o = 0
        offset = 0
        if 'pag' in params:
            offset = int(params['pag']) * 20
        for classe in session.query(obj).order_by(obj.id)[int(offset): 20 + int(offset)]:
            for j in args:
                i[o][j] = (getattr(classe, j))
            o = o + 1
        return i

    def retreaveId(self, args, params, obj):
        session = bd()
        i = collections.defaultdict(dict)
        classe = session.query(obj).get(params['id'])
        for j in args:
            i[j] = (getattr(classe, j))
        return i

    def retreaveGenero(self, args, params, obj):
        session = bd()
        i = collections.defaultdict(dict)
        o = 0
        offset = 0
        if 'pag' in params:
            offset = int(params['pag']) * 20
        for classe in session.query(obj).order_by(obj.id).filter(Genero.nome.like("%" + params['genero'] + "%"))[
                      int(offset): 20 + int(offset)]:
            for j in args:
                i[o][j] = (getattr(classe, j))
            o = o + 1
        return i

    def retreaveNome(self, args, params, obj):
        session = bd()
        i = collections.defaultdict(dict)
        o = 0
        offset = 0
        if 'pag' in params:
            offset = int(params['pag']) * 20
        for classe in session.query(obj).order_by(obj.id).filter(obj.nome.like("%" + params['nome'] + "%"))[
                      int(offset): 20 + int(offset)]:
            for j in args:
                i[o][j] = (getattr(classe, j))
            o = o + 1
        return i

