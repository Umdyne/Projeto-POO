import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi


class TelaInicial(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('interface_ui.py', self)  # Carrega a interface a partir do arquivo .py

        # Conecta os botões aos métodos correspondentes
        self.botao_login.clicked.connect(self.abrir_tela_login)
        self.botao_registro.clicked.connect(self.abrir_tela_registro)
        self.botao_fechar.clicked.connect(self.fechar_janela)

    def abrir_tela_login(self):
        print("Botão Login pressionado")

    def abrir_tela_registro(self):
        print("Botão Registro pressionado")

    def fechar_janela(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_inicial = TelaInicial()
    tela_inicial.show()
    sys.exit(app.exec_())
