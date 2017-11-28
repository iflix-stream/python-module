from cerberus import Validator


class SerieValidate():
    def validaPost(self,args):
        v = Validator()
        schema = {
            'nome': {
                'required': True
            },
            'genero': {
                'required': True,
                'type': 'integer'
            },
            'classificacao': {
                'required': True,
                'type': 'integer'
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