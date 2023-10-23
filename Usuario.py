class Usuario:
    __slots__ = ['_nome', '_user', '_senha', '_email']

    def __init__(self, nome, user, senha, email):
        self._nome = nome
        self._user = user
        self._senha = senha
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, novo_user):
        self._user = novo_user

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email


