import json

import falcon
from util.DecodeReq import parse
from dao.FilmeDAO import FilmeDAO
from validate.FilmeValidate import FilmeValidate

class FilmeResource:
    def on_get(self, req, resp):
        resp.body = json.dumps(FilmeDAO().retreave(req.params))
        resp.set_header('Content-Type', 'application/json')
        resp.content_type = "application/json"
        resp.status = falcon.HTTP_OK

    def on_post(self, req, resp):
        content = parse(req)
        valueValidated = FilmeValidate().validaPost(content)
        if (valueValidated == True):
            FilmeDAO().create(content)
            resp.status = falcon.HTTP_CREATED
        else:
            resp.body = json.dumps(valueValidated)
            resp.status = falcon.HTTP_400
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')

    def on_put(self, req, resp):
        result = parse(req)
        resp.status = falcon.HTTP_400
        if (FilmeValidate().validaPut(req.params)):
            result['id'] = req.params['id']
            FilmeDAO().update(result)
            resp.status = falcon.HTTP_NO_CONTENT
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_400
        if (FilmeValidate().validaDelete(req.params)):
            FilmeDAO().delete(req.params['id'])
            resp.status = falcon.HTTP_NO_CONTENT
        resp.content_type = "application/json"
        resp.set_header('Content-Type', 'application/json')
