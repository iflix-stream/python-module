from passlib.hash import bcrypt, bcrypt_sha256
from iflix.dao.ModeloDAO import ModeloDAO
from iflix.models.Usuario import Usuario
from iflix.models.banco import bd


class UsuarioDAO:
    def retreave(self, args):
        return ModeloDAO().retreave(args=[Usuario.id.name, Usuario.nome.name, Usuario.email.name], params=args,
                                    obj=Usuario)

    def create(self, result):
        session = bd()
        usuario = Usuario(nome=result['nome'], avatar=result['avatar'], isControleDosPais=result['isControleDosPais'],
                          senha=result['senha'], email=result['email'],
                          dataNascimento=result['dataNascimento'])
        session.add(usuario)
        session.commit()

    def update(self, result):
        session = bd()
        usuario = session.query(Usuario).get(result['id'])
        if 'nome' in result:
            usuario.nome = result['nome']
        if 'avatar' in result:
            usuario.avatar = result['avatar']
        if 'senha' in result:
            usuario.senha = result['senha']
        if 'email' in result:
            usuario.email = result['email']
        if 'dataNascimento' in result:
            usuario.dataNascimento = result['dataNascimento']
        session.commit()

    def delete(self, arg):
        session = bd()
        usuario = session.query(Usuario).get(arg)
        session.delete(usuario)
        session.commit()
