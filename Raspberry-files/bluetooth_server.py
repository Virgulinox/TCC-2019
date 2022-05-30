from bluetooth import *

mac_address = '80:7D:3A:98:EC:76'

server_socket = BluetoothSocket(RFCOMM)
server_socket.bind(mac_address)
server_socket.listen()

client_socket, address = server_socket.accept()

data = str(client_socket.recv(1024))

print("received [%s]" % data)

client_socket.close()
server_socket.close()