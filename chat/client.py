import socket
import threading


#Choosing Nickname
nickname = input("Choose your nickname: ")

#Connecting to Server
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',55556))


def recieve():
    while True:
        try:
            # Receive Message from Server
            # IF 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection when Error
            print('An Error occured!')
            client.close()
            break
# Sending Messages to Server
def write():
    while True:
        message = '{}: {}'.format(nickname,input(''))
        client.send(message.encode('ascii'))

# Starting Threads for Listening and Writing
recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
