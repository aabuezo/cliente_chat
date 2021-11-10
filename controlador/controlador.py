import socket
import sys
import threading

contactos = ['Pablo     ', 'Alejandro ']
lista_mensajes = []
nombre = 'Juan      '


class Client:
    def __init__(self, host='localhost', port=3000):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect( (host, port))
        self._receive = threading.Thread(target=self.receive)
        self._receive.daemon = True
        self._receive.start()
        # while True:
        #     self.send()

    def receive(self):
        while True:
            packet = self._socket.recv(1024)
            if packet:
                data = packet.decode('utf-8')
                sender = data[:10].rstrip()
                text = data[10:]
                msg = sender + ': ' + text
                self.actualizar_lista_mensajes(msg)
                print(msg)

    def send(self):
        msg = input('Mensaje: ')
        if msg == 'salir':
            self._socket.close()
            sys.exit()
        else:
            self._socket.send(msg.encode('utf-8'))

    def enviar_mensaje(self, msg):
        self._socket.send(msg.encode('utf-8'))

    def actualizar_lista_mensajes(self, msg):
        lista_mensajes.append(msg)


if __name__ == '__main__':
    cli = Client()