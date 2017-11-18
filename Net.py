import falcon
from controllers.Filme import FilmeResource
from controllers.Requisicao import RequisicaoResource

api = falcon.API()
api.add_route('/filme', FilmeResource())
api.add_route('/requisicao', RequisicaoResource())
