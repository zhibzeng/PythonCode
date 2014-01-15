import socket
s = socket.socket()
host = '127.0.0.1'
port = 12345
s.bind((host,port))
s.listen(5)#waiting list number
while(True):
    client,address = s.accept()
    print('get connection from ',address)
    client.send('thank you for connecting')
    client.close()
    


