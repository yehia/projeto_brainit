import os
import psycopg2

def create():
    connection = psycopg2.connect(
        host = os.environ.get('DB_HOST'),
        database = os.environ.get('DB_NAME'),
        user = os.environ.get('DB_USER'),
        password = os.environ.get('DB_PASS'),
        port='5432'
    )

    return connection