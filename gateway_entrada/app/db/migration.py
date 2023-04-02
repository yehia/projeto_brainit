import logging
import db_connection

TABLE_COMANDO_PENDENTE = '''
    CREATE TABLE comando_pendente(
        id SERIAL,
        mensagem TEXT NOT NULL
    )
'''

TABLE_MSG_RECEBIDA_QUERY = '''
    CREATE TABLE mensagem_recebida(
        id SERIAL,
        mensagem TEXT NOT NULL
    )
'''

TABLE_MSG_TRATADA = '''
    CREATE TABLE mensagem_tratada(
        id SERIAL,
        campo1 TEXT NOT NULL,
        campo2 TEXT NOT NULL,
        campo3 TEXT NOT NULL,
        campo4 TEXT NOT NULL
    )
'''

connection = db_connection.create()

pointer = connection.cursor()

try:
    pointer.execute(TABLE_COMANDO_PENDENTE)
    pointer.execute(TABLE_MSG_RECEBIDA_QUERY)
    pointer.execute(TABLE_MSG_TRATADA)
    connection.commit()
    logging.info('TABELA CRIADA')

except Exception as e:
    logging.error('TABELA DUPLICADA ', e)

finally:
    connection.close()