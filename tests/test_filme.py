import falcon
import requests
def test_post_filme():
    test_filme = {
        'nome':'Filme teste',
        'classificacao':'14',
        'caminho':'em um lugar ai',
        'duracao':'2:50',
        'sinopse':'filmequalquer',
        'thumbnail':'google.com',
        'genero_id':1
    }
    response = requests.post(
        'http://localhost:8000/filme',
        data=test_filme
    )
    assert response.status_code == falcon.HTTP_CREATED