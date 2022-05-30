import socket

serverMACAddress = '80:7D:3A:98:EC:76' #Esp32 MAC ADRESS
port = 1

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

while True:
    text = str(s.recv(1024))
    x = text.split('b')
    string = x[1].split("'")

    bpm = 0

    try:
        bpm = int(string[1])
        print(bpm)
    except:
        bpm = 0

s.close()