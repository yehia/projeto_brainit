import socket


HEADER = 256 # Tamanho da String... cada char possui 1 byte
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT' # Mensagem que deve ser passada através do client para se desconectar do socket
SERVER = '192.168.1.113'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send('29InbGFKBAy;dwP8YakzZ&Ty;RC0H3ByUqV8Uz!;9BnIwQUw!zvhu')
input()
send('CXYn8QAVVt4;k7^$G25X!M09;O$kYh62tR*dW3I;@4ofbO7^cpxgF')
input()
send('AaB#xpt4#XX;8AWKY1ynQn#2;ut133zwYi%B8HY;p4N*Jb8RMSGaJ')

send(DISCONNECT_MESSAGE)