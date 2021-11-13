import socket
import sys
import threading


class Notificacion(Exception):
    pass


class Client:
    def __init__(self, host='localhost', port=3000):
        self.contactos = ['Turnos Med', '          ']
        self.mensajes = []
        self.nombre = 'Yo        '
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect( (host, port))
        # self._recv = threading.Thread(target=self.recibir_mensaje)
        # self._recv.daemon = True
        # self._recv.start()

    def recibir_mensaje(self):
        while True:
            packet = self._socket.recv(1024)
            if packet:
                data = packet.decode('utf-8')
                sender = data[:10].rstrip()
                text = data[10:]
                msg = sender + ': ' + text
                self.mensajes.append(msg)
                print(msg)
                raise Notificacion

    def enviar_mensaje(self, msg):
        self._socket.send(msg.encode('utf-8'))
