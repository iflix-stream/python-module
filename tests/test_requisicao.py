import requests
import json

def test_post_ping():
    response = requests.post('http://localhost:8000/requisicao')
    responseJson = response.json()
    assert response.status_code == 200
    assert 'url' in responseJson
    assert 'token' in responseJson