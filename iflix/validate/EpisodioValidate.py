from cerberus import Validator


class EpisodioValidate():
    def validaPost(self, args):
        v = Validator()
        schema = {
            'nome': {
                'required': True
            },
            'sinopse': {
                'required': True
            },
            'temporada': {
                'required': True
            },
            'duracao': {
                'required': True
            },
            'caminho': {
                'required': True
            },
            'serie': {
                'required': True
            },
            'numero': {
                'required': True
            }
        }
        if (v.validate(args, schema)):
            return True
        return v.errors

    def validaPut(self, args):
        if ('id' in args):
            return True
        return False

    def validaDelete(self, args):
        if ('id' in args):
            return True
        return False
