import json

def parse(req):
    result = {}
    try:
        result = json.loads(req.stream.read(), encoding='utf-8')
    except:
        result = {}
    return result
