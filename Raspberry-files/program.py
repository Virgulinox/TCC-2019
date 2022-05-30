# Main code to data acquisition
import socket
import FaBo9Axis_MPU9250
import sys
from datetime import datetime
import time

mpu9250 = FaBo9Axis_MPU9250.MPU9250()
loop_control = True
s = socket.socket()
conn_esp32 = False


athlete = ['0', 'description']
_input = input("Insert the athlete's ID and a description: ")
athlete = _input.split(';')

data_hr = datetime.now().strftime('%d-%m-%Y_%H-%M')
file_name = athlete[0] + "_" + athlete[1] + "_" + data_hr + ".txt"
file = open(file_name, 'w+')

print("Created file "+file_name)

timeout = time.time() + 60*2

while True:

    try:
        serverMACAddress = '80:7D:3A:98:EC:76'  # Esp32 MAC ADRESS
        port = 1
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.connect((serverMACAddress, port))
        print("Connection with ESP32 OK!")
        conn_esp32 = True

    except Exception as e:
        print(str(e))
        conn_esp32 = False

    try:

        bpm = 0

        while time.time() < timeout:

            test = 0

            accel = mpu9250.readAccel()

            if(conn_esp32 == True):
                text = str(s.recv(1024))
                x = text.split('b')
                string = x[1].split("'")
                string2 = string[1]
                string3 = string2.split("\\")

                try:
                    bpm = int(string3[0])

                except Exception as e:
                    x = 0

            data = str(accel['z']) + ", " + str(bpm)
            print(data)
            file.write(data + "\n")

            time.sleep(0.1)

        sys.exit()

    except Exception as e:
        print(str(e))
        sys.exit()
