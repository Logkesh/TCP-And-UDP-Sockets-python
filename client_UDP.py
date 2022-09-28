from socket import socket, gethostname,SOCK_DGRAM,AF_INET

s = socket(AF_INET,SOCK_DGRAM)
host = gethostname()
port = 12345
msg = ""

while True:
    msg = input("Enter Msg: ") 
    s.sendto(msg.encode("utf-8"),(host,port))

    if(msg == 'quit'):
        break

    msg,addr = s.recvfrom(1024)
    print("Message from Server({}): {}".format(addr,msg.decode("utf-8")))
    
