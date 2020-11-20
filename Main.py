import RemoteIP
import LocalIP


loop = True

while loop:
    remoteHost = input("Enter an address to check or 'exit': ").lower()

    if remoteHost == "exit":
        exit(0)

    print("{}: {}".format(remoteHost, RemoteIP.getIP(remoteHost)))
    print("Local IP Address: {}".format(LocalIP.getIP()))

exit(0)
