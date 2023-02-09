import socket
import threading

#connection Data
host = '127.0.0.1'
port = 55556

#Starting Server

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
#AF_INET indicates that we are using internet socket rather than an unix socket
#SOCK_STREAM indicates that we are using TCP not UDP
# List For Clients and thier nicknames
clients = []
nicknames = []
#Sending Message to All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

#Handling Messages From Clients
def handle(client):
    while True:
        try:
            #Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing and Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break
# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        #Print and Broadcast Nickname
        print('Nickname is {}'.format(nickname))
        broadcast('{} joined!'.format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive_thread = threading.Thread(target=receive)
receive_thread.start()
