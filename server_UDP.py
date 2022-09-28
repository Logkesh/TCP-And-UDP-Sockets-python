from socket import AF_INET,SOCK_DGRAM,gethostname,socket,gethostbyaddr

def send(msg : str):
    s.sendto(msg.encode("utf-8"),addr)

s = socket(AF_INET,SOCK_DGRAM)

host = gethostname()

port = 12345

s.bind((host,port))

msg = ""

while(msg != "quit"):
    print("Waiting For Client!!!")
    msg,addr = s.recvfrom(1024)
    msg = msg.decode("utf-8")
    print("Message from ",addr,":",msg)

    if msg.startswith('addr'): send("Address: "+str(addr))
    
    elif msg.startswith('hi'): send('Hello! Client')
    
    elif msg == 'quit': 
        send('Bye Client!!')
        break
    else:
        send(input("What to say? "))