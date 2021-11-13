from controlador.controlador import Client, Notificacion
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import threading
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
        self.cliente = Client()
        self.destinatario = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(271, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.actualizar = threading.Thread(target=self.actualizar_lista_mensajes)
        self.actualizar.daemon = True

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
        self.combo_contactos.addItems(self.cliente.contactos)
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
        self.actualizar.start()

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

        self._recv = threading.Thread(target=self.recibir_mensaje)
        self._recv.daemon = True
        self._recv.start()

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
        if texto != '':
            mensaje = self.cliente.nombre + texto
            self.cliente.enviar_mensaje(mensaje)
            self.cliente.mensajes.append(self.cliente.nombre.rstrip() + ': ' + texto)
            self.actualizar_lista_mensajes()
            print(texto)
            self.texto_mensaje.setText('')

    def recibir_mensaje(self):
        while True:
            try:
                self.cliente.recibir_mensaje()
            except Notificacion:
                self.actualizar_lista_mensajes()
                # self.recibir_mensaje()
            finally:
                pass

    def actualizar_lista_mensajes(self):
        self.lista_mensajes.clear()
        self.lista_mensajes.addItems(self.cliente.mensajes)


