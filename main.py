import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.85"
port = 135

def portscanner(port):
    if soc.connect_ex((host, port)):
        print("Port " + str(port) + " is closed")
    else:
        print("Port " + str(port) + " is opened")

portscanner(port)

