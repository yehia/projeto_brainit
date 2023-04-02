import schedule
import logging

from db import db_connection

def handle():
    connection = db_connection.create()
    pointer = connection.cursor()
    pointer.execute("SELECT * FROM comando_pendente")
    rows = pointer.fetchall()

    for r in rows:
        try:
            id = r[0]
            msg = r[1].split(';')
            print(f'[TRATAMENTO] TRATANDO MENSAGEM {msg}')
            pointer.execute(f"INSERT INTO mensagem_tratada(campo1, campo2, campo3, campo4) VALUES('{msg[0]}','{msg[1]}','{msg[2]}','{msg[3]}')")
            pointer.execute(f"DELETE FROM comando_pendente WHERE id = {id}")
            connection.commit()
        except Exception as e:
                    logging.error('ERRO AO MANIPULAR MENSAGEM ', e)


schedule.every(20).seconds.do(handle)

print('INICIANDO JOB...')
while True:
    schedule.run_pending()