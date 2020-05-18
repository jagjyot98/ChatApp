import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input(str("please enter hostname of server:"))  # taking system name to connect with
s.connect((host, 1234))  # sending connection request to server for connection
print("Connected to chat server")
while 1:
    msg = s.recv(1024)   # recieving messages from server
    msg = msg.decode()     # decpoding recieved messages from binary form to 'utf-8'
    print("Server:", msg, end="\n\n")

    message = input(str(">>"))
    message = message.encode()   # encoding m.essage to be send from 'utf-8' to binary
    s.send(message)    # sending message after encoding
    print("Sent..", end="\n\n")
    