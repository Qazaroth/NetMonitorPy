import socket


def getIP(hostname):
    IP = None

    try:
        IP = socket.gethostbyname(hostname)
    except:
        IP = "Offline"

    return IP
