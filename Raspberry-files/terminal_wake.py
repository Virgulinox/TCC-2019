from bluetooth import *
import os

while True:

    try:
        server_socket = BluetoothSocket(RFCOMM)
        server_socket.bind(("", 1))
        server_socket.listen(1)
        client_socket, address = server_socket.accept()
        client_socket.close()
        server_socket.close()

    except:
        x = 0


