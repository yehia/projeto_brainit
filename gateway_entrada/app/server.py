import socket
import threading
import logging

from db import db_connection

HEADER = 256 # Tamanho da String... cada char possui 1 byte
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT' # Mensagem que deve ser passada através do client para se desconectar do socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f'[NOVA CONEXÃO] {addr} conectado.')

    connection = db_connection.create()
    pointer = connection.cursor()
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connection.close()
                connected = False
            else:
                try:
                    pointer.execute(f"INSERT INTO mensagem_recebida(mensagem) VALUES('{msg}')")
                    pointer.execute(f"INSERT INTO comando_pendente(mensagem) VALUES('{msg}')")
                    connection.commit()
                except Exception as e:
                    logging.error('ERRO AO INSERIR DADO ', e)

            print(f'[{addr}] {msg}')
            conn.send(f'[MENSAGEM RECEBIDA] {msg}'.encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f'[ESCUTANDO] Server está escutando em {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[CONEXÕES ATIVAS] {threading.active_count() - 1}')


print('[INICIANDO] server inicializado...')
start()