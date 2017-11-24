import json

import falcon

from iflix.dao.GeneroDAO import GeneroDAO
from iflix.util.DecodeReq import parse
from iflix.validate.GeneroValidate import GeneroValidate


class GeneroResource:
    def on_get(self, req, resp):
        resp.body = json.dumps(GeneroDAO().retreave(req.params))
        resp.set_header('Content-Type', 'application/json')
        resp.content_type = "application/json"
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        content = parse(req)
        valueValidated = GeneroValidate().validaPost(content)
        if valueValidated == True:
            GeneroDAO().create(content)
            resp.status = falcon.HTTP_CREATED
        else:
            resp.body = json.dumps(valueValidated)
            resp.status = falcon.HTTP_400
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')

    def on_put(self, req, resp):
        result = parse(req)
        resp.status = falcon.HTTP_400
        if GeneroValidate().validaPut(req.params):
            result['id'] = req.params['id']
            GeneroDAO().update(result)
            resp.status = falcon.HTTP_NO_CONTENT
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_400
        if GeneroValidate().validaDelete(req.params):
            GeneroDAO().delete(req.params['id'])
            resp.status = falcon.HTTP_NO_CONTENT
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')
