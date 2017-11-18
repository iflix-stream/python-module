import falcon
import requests


def test_get_filme():
    response = requests.get('http://localhost:8000/filme')
    assert response.status_code == 200


def test_post_filme_certo():
    test_filme = {
        'nome': 'Filme teste',
        'classificacao': '14',
        'caminho': 'em um lugar ai',
        'duracao': '2:50',
        'sinopse': 'filmequalquer',
        'thumbnail': 'google.com',
        'genero_id': 1
    }
    response = requests.post(
        'http://localhost:8000/filme',
        data=test_filme
    )
    assert response.status_code == 201


def test_post_filme_errado():
    test_filme = {
        'nome': 'Filme teste',
        'classificacao': '14',
        'caminho': 'em um lugar ai',
        'duracao': '2:50',
        'sinopse': 'filmequalquer',
        'thumbnail': 'google.com',
        'genero_id': 1
    }
    response = requests.post(
        'http://localhost:8000/filme',
        data=test_filme
    )
    assert response.status_code != 201
