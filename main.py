import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(0.5)

host = input("What is the IP address you'd like to scan?: ")


def portscanner(port):
    if soc.connect_ex((host,port)):
        print("Port " + str(port) + " is closed")
    else:
        print("Port " + str(port) + " is open")

for port in range(1,1000):
    portscanner(port)

