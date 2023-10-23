import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from telaCadastro import Tela_Cadastro
from telaLogin import Tela_Login
from telaInicial import Tela_Inicial
from telaLoginRealizado import Login_Realizado
from sistema import Sistema
from Usuario import Usuario

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack2)

        self.dentro = Login_Realizado()
        self.dentro.setupUi(self.stack3)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)


        self.cad = Sistema()
        self.tela_inicial.Botao_Cadastro.clicked.connect(self.abrirTelaCadastro) # funções dos botões da tela principal
        self.tela_inicial.Botao_Login.clicked.connect(self.abrirTelaLogin)

        self.tela_cadastro.Botao_cadastrar.clicked.connect(self.botaoCadastra)
        self.tela_cadastro.Botao_Voltar.clicked.connect(self.voltarCadastro)
        self.tela_login.Botao_Entrar.clicked.connect(self.logar)
        self.tela_inicial.Botao_Sair.clicked.connect(sys.exit)

        self.dentro.Botao_Sair.clicked.connect(self.sairSistema)
        self.tela_cadastro.Botao_Voltar.clicked.connect(self.voltarCadastro)
        self.tela_login.Botao_Voltar.clicked.connect(self.voltarLogin)

    def botaoCadastra(self):
        nome = self.tela_cadastro.caixa_nome.text()
        user = self.tela_cadastro.caixa_email.text()
        senha = self.tela_cadastro.caixa_senha.text()
        email = self.tela_cadastro.caixa_usuario.text()
        if not(nome == '' or email == '' or senha == '' or user == ''):
            if self.cad.checkUser(user):
                QMessageBox.information(None,'POOII', 'Nome de usuário já cadastrado!')
                self.tela_cadastro.caixa_email.setText('')
            else:
                usuario = Usuario(nome, email, senha, user)
                self.cad.cadastrar(usuario)
                QMessageBox.information(None,'POOII', 'Cadastro realizado com sucesso!')
                self.tela_cadastro.caixa_email.setText('')
                self.tela_cadastro.caixa_nome.setText('')
                self.tela_cadastro.caixa_senha.setText('')
                self.tela_cadastro.caixa_usuario.setText('')
                self.QtStack.setCurrentIndex(0)
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')

        # self.QtStack.setCurrentIndex(0)
    
    def logar(self):
        user = self.tela_login.caixa_usuario.text()
        senha = self.tela_login.caixa_senha.text()
        if self.cad.checkPassword(user, senha):
            self.QtStack.setCurrentIndex(3)
        else:
            QMessageBox.information(None,'POOII', 'Login ou senha errados!')
            self.tela_login.caixa_senha.setText('')
            self.tela_login.caixa_usuario.setText('')
        
    

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaLogin(self):
        self.QtStack.setCurrentIndex(2)
        self.tela_login.caixa_senha.setText('')
        self.tela_login.caixa_usuario.setText('')
    
    def sairSistema(self):
        self.QtStack.setCurrentIndex(0)
    
    def voltarCadastro(self):
        self.QtStack.setCurrentIndex(0)
        self.tela_cadastro.caixa_usuario.setText('')
        self.tela_cadastro.caixa_nome.setText('')
        self.tela_cadastro.caixa_senha.setText('')
        self.tela_cadastro.caixa_email.setText('')
    
    def voltarLogin(self):
        self.QtStack.setCurrentIndex(0)
        self.tela_login.caixa_senha.setText('')
        self.tela_login.caixa_usuario.setText('')

    
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
