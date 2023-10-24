import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from tela_cadastro import Tela_Cadastro
from tela_inicial import Tela_Inicial
from sistema import Sistema
from usuario import Usuario
from mensagens import Mensagens
from tela_principal import Tela_Principal
from tela_perfil import Tela_Perfil

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_principal = Tela_Principal()
        self.tela_principal.setupUi(self.stack3)

        self.tela_perfil = Tela_Perfil()
        self.tela_perfil.setupUi(self.stack4)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)
        

        self.cad = Sistema()
        self.tela_inicial.botao_ir_cadastro.clicked.connect(self.abrirTelaCadastro) # funções dos botões da tela principal
        # self.tela_inicial.Botao_Login.clicked.connect(self.abrirTelaLogin)
        self.tela_inicial.botao_logar.clicked.connect(self.logar)

        self.tela_cadastro.botao_ir_cadastro.clicked.connect(self.botaoCadastra)
        self.tela_cadastro.botao_sair.clicked.connect(self.voltarCadastro)
        
        self.tela_principal.botao_perfil.clicked.connect(self.abrirPerfil)
        self.tela_cadastro.botao_sair.clicked.connect(self.voltarCadastro)

        self.tela_principal.botao_postar.clicked.connect(self.postar)

        self.tela_perfil.botao_inicio.clicked.connect(self.abrirTelaPrincipal)
        self.tela_perfil.botao_sair.clicked.connect(self.abrirTelaInicial)
        
        self.tela_inicial.botao_sair.clicked.connect(QtWidgets.qApp.quit)

    def botaoCadastra(self):
        nome = self.tela_cadastro.caixa_nome.text()
        email = self.tela_cadastro.caixa_email.text()
        senha = self.tela_cadastro.caixa_senha.text()
        user = self.tela_cadastro.caixa_usuario.text()
        if not(nome == '' or email == '' or senha == '' or user == ''):
            if self.cad.cadastrado(user):
                QMessageBox.information(None,'POOII', 'Nome de usuário já cadastrado!')
                self.tela_cadastro.caixa_usuario.setText('')
            else:
                usuario = Usuario(nome, user, senha, email)
                self.cad.cadastrar(usuario)
                QMessageBox.information(None,'POOII', 'Cadastro realizado com sucesso!')
                self.tela_cadastro.caixa_email.setText('')
                self.tela_cadastro.caixa_nome.setText('')
                self.tela_cadastro.caixa_senha.setText('')
                self.tela_cadastro.caixa_usuario.setText('')
                self.QtStack.setCurrentIndex(0)
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')

    
    
    def logar(self):
        user = self.tela_inicial.caixa_usuario.text()
        senha = self.tela_inicial.caixa_senha.text()
        usuario = self.cad.checkPassword(user, senha)
        if usuario != False:
            self.QtStack.setCurrentIndex(3)
            self.tela_perfil.Nome.setText(usuario.user)
            self.tela_perfil.Email.setText(usuario.email)
        else:
            QMessageBox.information(None,'POOII', 'Login ou senha errados!')
            self.tela_inicial.caixa_senha.setText('')
            self.tela_inicial.caixa_usuario.setText('')
        
    def postar(self):
        post = self.tela_principal.texto_postar.toPlainText()
        QMessageBox.information(None,'POOII', 'Mensagem Postada!')
        usuario = self.tela_perfil.Nome.text()
        m = Mensagens(post, usuario)
        print(f'{m._mensagem}, {m._perfil}, {m._data}')
        self.tela_principal.texto_postar.setText('')
        pass

    def abrirPerfil(self):
        self.QtStack.setCurrentIndex(4)
        self.tela_inicial.caixa_senha.setText('')
    
    def abrirTelaInicial(self):
        self.QtStack.setCurrentIndex(0)
    
    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaLogin(self):
        self.QtStack.setCurrentIndex(2)
    
    def sairSistema(self):
        self.QtStack.setCurrentIndex(0)
    
    def abrirTelaPrincipal(self):
        self.QtStack.setCurrentIndex(3)
    
    def voltarCadastro(self):
        self.QtStack.setCurrentIndex(0)
        self.tela_cadastro.caixa_usuario.setText('')
        self.tela_cadastro.caixa_nome.setText('')
        self.tela_cadastro.caixa_senha.setText('')
        self.tela_cadastro.caixa_email.setText('')
    
    def voltarLogin(self):
        self.QtStack.setCurrentIndex(0)
        self.tela_inicial.caixa_senha.setText('')
        self.tela_inicial.caixa_usuario.setText('')
    
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
