from iflix.models.Filme import Filme
from iflix.models.banco import bd
import collections


class ModeloDAO:
    def retreave(self, args, params,obj):
        #faltando arrumar  limite  para dps adicionar o resto das query nas funções
        if ('id' in params):
            return self.retreaveId(args)
        elif ('genero' in params):
            return self.retreaveGenero(args)
        elif ('nome' in params):
            return self.retreaveNome(args)

        return self.retreaveAll(args,params,obj)

    def retreaveAll(self, args,params,obj):
        session = bd()
        i = collections.defaultdict(dict)
        o = 0
        offset = 0
        if ('de' in params):
            offset = params['de']
        for classe in session.query(obj).order_by(obj.id).offset(0):
            for j in args:
                i[o][j] = (getattr(classe, j))
            o = o + 1
        return i

    def retreaveId(self, args):
        pass

    def retreaveGenero(self, args):
        pass

    def retreaveNome(self, args):
        pass
