import falcon
from controllers.FilmeController import FilmeResource

api = falcon.API()
api.add_route('/filme', FilmeResource())
