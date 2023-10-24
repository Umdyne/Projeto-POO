class Sistema:
    __slot__ = ['_usuarios']

    def __init__(self):
        self._usuarios = []
    

    def cadastrar(self, usuario):
        for pessoa in self._usuarios:
            if usuario.user == pessoa.user:
                return False 
        print(len(self._usuarios))
        self._usuarios.append(usuario)
        print(f'nome: {usuario.nome}, user: {usuario.user}, email: {usuario.email}, senha: {usuario.senha}')
        return True

    def cadastrado(self, user):
        for usuario in self._usuarios:
            if usuario.user == user:
                return True
        return False
    

    def checkUser(self, user):
        for curr in self._usuarios:
            if curr.user == user:
                print(user, '==', curr.user)
                return False
        
        return True
    
    def checkPassword(self, user, userpassword):
        print('checkpassword')
        print(f'teste: user: {user}, senha: {userpassword}')
        for user in self._usuarios:
            print(f'user: {user.user}, senha: {user.senha}')
            if (user.user == user and user.senha == userpassword):
                print('if')
                print(f'usuario {user.user}, user {user}\nsenha {user.senha}, password {userpassword}')
                return True
        
        return False
    
