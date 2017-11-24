from cerberus import Validator


class UsuarioValidate():
    def validaPost(self, args):
        v = Validator()
        schema = {
            'nome': {
                'required': True
            },
            'senha': {
                'required': True
            },
            'avatar': {
                'required': True
            },
            'isControleDosPais': {
                'required': True
            },
            'email': {
                'required': True
            },
            'dataNascimento': {
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
