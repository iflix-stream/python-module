from cerberus import Validator


class TemporadaValidate():
    def validaPost(self, args):
        v = Validator()
        schema = {
            'numero': {
                'required': True,
                'type': 'integer'
            },
            'serie': {
                'required': True,
                'type': 'integer'
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
