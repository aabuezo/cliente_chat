"""
    Autor: Alejandro A. Buezo
    Ultima modificación: 20-11-2021
"""
import socket


# si el servidor se ejecuta en otra maquina, se puede cambiar por la IP del servidor
# entre comillas - recordar habilitar el PORT en el firewall del servidor
HOST = 'localhost'
PORT = 3000


class Notificacion(Exception):
    """ se lanza esta excepcion cuando se quiere notificar que se recibio
        un nuevo mensaje via sockets """
    pass


class SinConexion(ConnectionError):
    """ se lanza si se perdio la conexión """
    pass


class Client:
    """ cliente sockets """
    def __init__(self, host=HOST, port=PORT):
        self.contactos = ['Turnos Med', '          ']
        self.mensajes = []
        self.nombre = 'Alejandro '
        self.separador = '-' * 50
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect( (host, port))

    def recibir_mensaje(self):
        """ metodo que procesa los mensajes entrantes """
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
                # le aviso a la vista que llegó un mensaje nuevo para que se actualice
                raise Notificacion

    def enviar_mensaje(self, msg):
        """ metodo para enviar mensajes """
        try:
            self._socket.send(msg.encode('utf-8'))
        except socket.error:
            # te enteras que se corto la conexion cuando queres enviar
            # sino se queda escuchando eternamente
            raise SinConexion()

    def get_nombre(self):
        """ obtiene el nombre del usuario de la aplicacion """
        return self.nombre
