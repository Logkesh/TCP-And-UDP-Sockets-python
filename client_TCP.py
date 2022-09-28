import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))


while True:
    print("Server: ", s.recv(1024).decode())
    
    msg = input("Enter the message: ")
    s.send(msg.encode('utf-8'))
    
    if msg == 'quit': 
        print("Server: ", s.recv(1024).decode())
        break

s.close()