import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1234))
# 1234 port number
print("Host Name:"+socket.gethostname())   # extracts system name
print("HOST IP ADDRESS:"+socket.gethostbyname('www.google.com'))  # extracts ip address
print("Server done binding to host and port successfully")
print("Server is waiting for incoming connection")
s.listen(1)
# clientsocket is the socket cell with which client wants to connect
# address is the ip address of client
clientsocket, address = s.accept()
# 'f' in the print statement is to display tuple address with the concatenated string
print(f"Connection from {address} has been established !")
while 1:
    message = input(str(">>"))
    message = message.encode()   # encoding of message before sending to client form "utf-8" to binary
    clientsocket.send(message)   # sending message to client after encoding
    print("Sent..", end="\n\n")

    # max amount of data to be send
    msg = clientsocket.recv(1024)  # recieving messege from client
    msg = msg.decode()       # encoding of message after recieving from client to "utf-8" from binary
    # utf-8 is the form in which the recieved mssg should be converted to be displayed
    print("Client:", msg, end="\n\n")
