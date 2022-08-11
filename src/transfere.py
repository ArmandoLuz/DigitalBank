from PyQt5 import uic
from dataBase import db

class Transfere:

    def __init__(self, AppWindow):
        #Chamando o self da classe que contem a stack
        self._appWindow = AppWindow

        #Carregando a ui da tela de deposito
        self._window = uic.loadUi("../uis/TelaTransferir.ui")

        #Carregando os botoes
        self._backTrans = self._window.button_back_trans
        self._buttonTrans = self._window.buttonTrans

        #carregando os lineEdits
        self._valor = self._window.inputValorTrans
        self._destino = self._window.inpNumTrans

        #Carregando os eventos
        self._load_events()

    @property
    def window(self):
        return self._window
    
    def _load_events(self):
        self._backTrans.clicked.connect(lambda: self.back())
        self._buttonTrans.clicked.connect(lambda: self.transfere())

    def _load_info(self, account):
        self._account = account
    
    def back(self):
        #Reseta os campos
        self._valor.setText("")
        self._destino.setText("")
        self._window.labelTransStts.setText("")

        #Faz o retorno para a dashboard
        self._appWindow._dash._load_info(self._account)
        self._appWindow.go_to(3)

    def transfere(self):
        #Buscando o destinatario
        if self._destino.text() == "" or self._valor.text() == "":
            self._window.labelTransStts.setText("Insira todos os dados!")
            return 0
        else:
            destino = database.busca_user(int(self._destino.text()))

        if destino != None:
            status = self._account.transfere(destino, float(self._valor.text()))
            self._window.labelTransStts.setText(status)
            self._window.inputValorTrans.setText("")
            self._window.inpNumTrans.setText("")
        else:
            self._window.labelTransStts.setText("conta não encontrada!")
            self._window.inputValorTrans.setText("")
            self._window.inpNumTrans.setText("")