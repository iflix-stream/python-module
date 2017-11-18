import falcon
import subprocess
import json
import re

class RequisicaoResource:
    def on_post(self, req, resp):

        hostname = {
            0: {
                'url':'google.com',
                'shortUrl':'10.1.6.23/ifix'
            }
        }
        for key in hostname:
            command = "ping -c 3 " + hostname[key]['url']
            pingResponse = subprocess.check_output(command, shell=True)
            matches = re.findall(" time=([\d.]+) ms", pingResponse)
            matches = [float(match) for match in matches]
            ms = sum(matches) / len(matches)
            print ms
        resp.body = json.dumps({'url':0,'token':'asd'})
        resp.set_header('Content-Type', 'application/json')
        resp.content_type = "application/json"
        resp.status = falcon.HTTP_OK
