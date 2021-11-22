# cliente_chat

TP Final de la Diplomatura de Python de la UTN - año 2021
Requerimientos: realizar un programa cliente/servidor usando patron MVC, clases, decoradores, sockets, ORM y BD SQLite.
Este repositorio corresponde al cliente, mientras que el servidor se encuentra en https://github.com/aabuezo/servidor_chat

Alumnos:
- Alejandro A. Buezo
- Luis A. Buezo

Descripción:
Se trata de un chat-bot para otorgar turnos.
El cliente y el servidor se ejecutan por separado, cada uno con su respectivo main.py en la carpeta raiz:

	- cliente/main.py
	- servidor/main.py
	
El cliente y el servidor se pueden ejecutar en maquinas distintas,
recordar cambiar el HOST en el archivo controlador.py (tanto en el cliente como en el servidor)
para que apunten a la IP del servidor.

Caso de uso:
- Servidor esperando conexion
- Cliente envia: hola!
- Servidor responde: Bienvenido al sistema de turnos! 
					Por favor ingrese su opcion:
					1. Obstetricia
					2. Oftalmologia
					etc
- Cliente envia su opcion
- Servidor responde con los turnos disponibles
- cliente envia su opcion
- Servidor reserva el turno en la BD y responde (maneja respuestas invalidas)
- Servidor cierra la conexion con el cliente
- Servidor queda a la escucha de nuevas conexiones
- El servidor se apaga escribiendo: salir (en el CMD)

Cada carpeta (cliente y servidor) tienen un archivo requerimientos.txt
donde se indica que se debe instalar y como ejecutar ambos.
