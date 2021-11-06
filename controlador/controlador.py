import socket
import sys
import threading


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
                msg = packet.decode('utf-8')
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


# datos de prueba - borrar!!!
lista_combo = ['Juan', 'Jose', 'Pedro', 'Mario']
lista_mensajes = [
    'Hola amigo',
    'como estas',
    'tanto tiemo?,'
    'todo bien?',
    'se te extraña loco!',
    'abrazo grande y',
    'espero verte pronto!',
    'esta es una linea muuuuuuy laaaaaaaaaaaaargaaaaaaaaaaaaaaaaaa de varias lineas para el ListWidget',
    'Hola amigo',
    'como estas',
    'tanto tiemo?,'
    'todo bien?',
    'se te extraña loco!',
    'abrazo grande y',
    'espero verte pronto!',
    'esta es una linea muuuuuuy laaaaaaaaaaaaargaaaaaaaaaaaaaaaaaa de varias lineas para el ListWidget',
    'Hola amigo',
    'como estas',
    'tanto tiemo?,'
    'todo bien?',
    'se te extraña loco!',
    'abrazo grande y',
    'espero verte pronto!',
    'esta es una linea muuuuuuy laaaaaaaaaaaaargaaaaaaaaaaaaaaaaaa de varias lineas para el ListWidget'
]


if __name__ == '__main__':
    cli = Client()