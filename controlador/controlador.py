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

import socket
import threading
import sys


class Cliente:

    def __init__(self, host='localhost', port=30000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))
        msg_recv = threading.Thread(target=self.recibir_mensaje)
        msg_recv.daemon = True
        msg_recv.start()

    def recibir_mensaje(self):
        pass
