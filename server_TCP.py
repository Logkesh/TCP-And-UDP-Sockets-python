import socket

PORT = 12345
HOST = socket.gethostname()

def send(msg):
    client.send(msg.encode('utf-8'))

s = socket.socket()
print("Socket successfully created")
s.bind((HOST,PORT))
s.listen(5)
client,addr = s.accept()
print("the socet successfully connected!!!",addr)

client.send('Hello Client'.encode('utf-8'))

while True:
    msg = client.recv(1024).decode('utf-8')
    print("Client: ", msg)

    if msg.startswith('addr'): send("Address: "+str(addr))
    
    elif msg.startswith('hi'): send('Hello! Client')
    
    elif msg == 'quit': 
        send('Bye Client!!')
        break
    else:
        send(input("What to say? "))
client.close()