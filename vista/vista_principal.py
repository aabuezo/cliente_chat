from controlador.controlador import lista_combo, lista_mensajes, Cliente
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


class App():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = VentanaPrincipal()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.salir()

    # modificado por Alejandro 31-10-2021
    def salir(self):
        sys.exit(self.app.exec_())


class VentanaPrincipal(object):
    def __init__(self):
        self.cliente = Cliente()
        self.destinatario = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(271, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # boton enviar
        self.boton_enviar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_enviar.setGeometry(QtCore.QRect(10, 350, 251, 31))
        self.boton_enviar.setObjectName("boton_enviar")
        self.boton_enviar.clicked.connect(self.enviar_mensaje)

        # combo contactos
        self.combo_contactos = QtWidgets.QComboBox(self.centralwidget)
        self.combo_contactos.setGeometry(QtCore.QRect(10, 10, 251, 23))
        self.combo_contactos.setObjectName("combo_contactos")
        # modificado por Alejandro 31-10-2021
        self.combo_contactos.addItems(lista_combo)
        self.combo_contactos.currentTextChanged.connect(self.combo_pressed)

        # texto a enviar
        self.texto_mensaje = QtWidgets.QTextEdit(self.centralwidget)
        self.texto_mensaje.setGeometry(QtCore.QRect(10, 300, 251, 41))
        self.texto_mensaje.setObjectName("texto_mensaje")

        # lista mensajes
        self.lista_mensajes = QtWidgets.QListWidget(self.centralwidget)
        self.lista_mensajes.setGeometry(QtCore.QRect(10, 40, 251, 251))
        self.lista_mensajes.setObjectName("lista_mensajes")
        # modificado por Alejandro 31-10-2021
        self.lista_mensajes.setWordWrap(True)
        self.lista_mensajes.addItems(lista_mensajes)

        # boton salir
        self.boton_salir = QtWidgets.QPushButton(self.centralwidget)
        self.boton_salir.setGeometry(QtCore.QRect(10, 390, 251, 31))
        self.boton_salir.setObjectName("boton_salir")
        # modificado por Alejandro 31-10-2021
        self.boton_salir.clicked.connect(lambda:MainWindow.close())

        # status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat Client"))
        self.boton_enviar.setText(_translate("MainWindow", "&Enviar Mensaje"))
        self.boton_salir.setText(_translate("MainWindow", "&Salir"))

    # modificado por Alejandro 31-10-2021
    def combo_pressed(self):
        self.destinatario = self.combo_contactos.currentText()
        print(self.destinatario)

    # modificado por Alejandro 1-11-2021
    def enviar_mensaje(self):
        texto = self.texto_mensaje.toPlainText()
        self.cliente.enviar_mensaje(texto)
        print(texto)
