import json

import falcon

from iflix.dao.TemporadaDAO import TemporadaDAO
from iflix.util.DecodeReq import parse
from iflix.validate.TemporadaValidate import TemporadaValidate


class TemporadaResource:

    def on_get(self, req, resp):
        resp.body = json.dumps(TemporadaDAO().retreave(req.params))
        resp.set_header('Content-Type', 'application/json')
        resp.content_type = "application/json"
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        content = parse(req)
        valueValidated = TemporadaValidate().validaPost(content)
        if valueValidated == True:
            TemporadaDAO().create(content)
            resp.status = falcon.HTTP_CREATED
        else:
            resp.body = json.dumps(valueValidated)
            resp.status = falcon.HTTP_400
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')

    def on_put(self, req, resp):
        result = parse(req)
        resp.status = falcon.HTTP_400
        if TemporadaValidate().validaPut(req.params) == True:
            result['id'] = req.params['id']
            TemporadaDAO().update(result)
            resp.status = falcon.HTTP_NO_CONTENT
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_400
        if TemporadaValidate().validaDelete(req.params) == True:
            TemporadaDAO().delete(req.params['id'])
            resp.status = falcon.HTTP_NO_CONTENT
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')
