import falcon

from iflix.controllers.ContagemController import ContagemResource
from iflix.controllers.FilmeController import FilmeResource
from iflix.controllers.GeneroController import GeneroResource
from iflix.controllers.SerieController import SerieResource
from iflix.controllers.UsuarioController import UsuarioResource

api = falcon.API()
api.add_route('/filme', FilmeResource())
api.add_route('/genero', GeneroResource())
api.add_route('/usuario', UsuarioResource())
api.add_route('/serie', SerieResource())
api.add_route('/contagem', ContagemResource())
