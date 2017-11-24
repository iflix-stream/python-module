import falcon

from iflix.controllers.FilmeController import FilmeResource
from iflix.controllers.GeneroController import GeneroResource
from iflix.controllers.UsuarioController import UsuarioResource

api = falcon.API()
api.add_route('/filme', FilmeResource())
api.add_route('/genero', GeneroResource())
api.add_route('/usuario', UsuarioResource())
