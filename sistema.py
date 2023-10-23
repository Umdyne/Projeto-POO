
class Sistema:
    __slot__ = ['_usuarios']

    def __init__(self):
        self._usuarios = []
    

    def cadastrar(self, usuario):
        for pessoa in self._usuarios:
            if usuario.user == pessoa.user:
                print(usuario.user,"==",pessoa.user)
                return False
        self._usuarios.append(usuario)
        print("")
        for n in self._usuarios:
            print(n.nome , n.user , n.email , n.senha)
        return True

    def cadastrado(self, user):
        for usuario in self._usuarios:
            if usuario.user == user:
                return True
        return False
    
    # def validationLogin(self, user, password):
    #     if self.checkUser(user):
    #         if self.checkPassword(password):
    #             return True

    #     return False   
    
    
    def checkUser(self, user):
        for curr in self._usuarios:
            if curr.user == user:
                return True
        
        return False
    
    def checkPassword(self, user, userpassword):
        for curr in self._usuarios:
            if curr.user == user and curr.senha == userpassword:
                return True
            
        
        return False
        
