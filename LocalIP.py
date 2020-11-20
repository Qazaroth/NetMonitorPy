import socket


def getIP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except :
        print("Error occured while fetching local ip.")
        return -1
