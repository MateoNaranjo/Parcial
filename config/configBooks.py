
import os
import sys
import sqlite3, random, datetime
import logging

# Asegura que el directorio raíz del proyecto esté en sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.Books import Book

logging.basicConfig(level=logging.INFO)

def getNewId():
    return random.getrandbits(28)




def connect():
    try:
        conn = sqlite3.connect(os.path.join(BASE_DIR, 'books.db'))
        logging.info('Conexión exitosa.')
        return conn
    except Exception as e:
        logging.warning(f'Conexión fallida: {e}')
        return None

conexion = connect()

def view():
    if not conexion:
        return []
    cur = conexion.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    books = []
    for i in rows:
        book = Book(i[0], True if i[1] == 1 else False, i[2], i[3])
        books.append(book)
    conexion.close()
    return books

libros = view()