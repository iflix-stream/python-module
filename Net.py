import falcon
import json

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
            ),
            'author': "adasdasds"
        }
        
        resp.body = json.dumps(quote)
        resp.set_header('Content-Type', 'application/json')
        resp.content_type = "application/json"

api = falcon.API()
api.add_route('/quote', QuoteResource())