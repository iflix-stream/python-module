import json

import falcon

from iflix.dao.ContagemDAO import ContagemDAO
from iflix.dao.FilmeDAO import FilmeDAO
from iflix.util.DecodeReq import parse
from iflix.validate.FilmeValidate import FilmeValidate
import socket

class ContagemResource:

    def on_get(self, req, resp):
        string = {'servidor':socket.gethostbyname(socket.gethostname())+":8080",'usuarios_online':ContagemDAO().retreave(req.params),'usuarios_permitidos':100}
        resp.body = json.dumps(string)
        resp.set_header('Content-Type', 'application/json')
        resp.content_type = "application/json"
        resp.status = falcon.HTTP_OK

