# ChatApp
A robust messenger app between a server and a client. Runs on Python Sockets. Fully User friendly.
I have provided many comments along with the code which will give you a basic idea about working of the program.
NOTE: This messenger app can currently run between those systems connected over SAME INTERNET CONNECTION or can run between different platforms for python over a single system. I am working on it to make it run over different internet connections and will soon update here also.
# Current Working
After creating both server and client files on your system... 
Run the Server code before Client code as the client will look for currently (then) running servers over the internet connection.
NOTE: Messaging can only be INITIATED by the Server. This can be changed by simply placing the message recieving code in Server before the sending one in the Server's infinite while loop. There, currently, first part is of sending a message and there after recieving part is given. You'll understand that easily with the comments in the code.
Similarly in client code also place the message sending part before the message recieving part.
And hence, messaging can now only be initiated by client side.
To know more about Python Sockets : 'https://docs.python.org/3.8/library/socket.html' 
