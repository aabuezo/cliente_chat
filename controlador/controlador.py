import socket


class Notificacion(Exception):
    pass


class SinConexion(ConnectionError):
    pass


class Client:
    def __init__(self, host='localhost', port=3000):
        self.contactos = ['Turnos Med', '          ']
        self.mensajes = []
        self.nombre = 'Alejandro '
        self.separador = '-' * 50
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect( (host, port))

    def recibir_mensaje(self):
        while True:
            packet = self._socket.recv(1024)
            if packet:
                data = packet.decode('utf-8')
                sender = data[:10].rstrip()
                text = data[10:]
                msg = sender + ': ' + text
                self.mensajes.append(msg)
                self.mensajes.append(self.separador)
                print(msg)
                raise Notificacion

    def enviar_mensaje(self, msg):
        try:
            self._socket.send(msg.encode('utf-8'))
        except socket.error:
            raise SinConexion()

