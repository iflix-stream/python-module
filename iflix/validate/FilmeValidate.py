from cerberus import Validator


class FilmeValidate():
    def validaPost(self,args):
        v = Validator()
        schema = {
            'nome': {
                'required': True
            },
            'genero': {
                'required': True
            },
            'caminho': {
                'required': True
            },
            'classificacao': {
                'required': True,
                'type': 'integer'
            },
            'duracao': {
                'required': True
            },
            'sinopse': {
                'required': True
            },
            'thumbnail': {
                'required': True
            }
        }
        if(v.validate(args, schema)):
            return True
        return v.errors
    def validaPut(self,args):
        if ('id' in args):
            return True
        return False
    def validaDelete(self,args):
        if ('id' in args):
            return True
        return False