import falcon
from controllers.Filme import FilmeResource
api = falcon.API()
api.add_route('/filme', FilmeResource())