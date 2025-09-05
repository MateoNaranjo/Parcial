import sqlite3, random, datetime

from models.Books import Book
import logging

logging.basicConfig(level=logging.INFO)

def getNewId():
    return random.getrandbits(28)



def connect():
    try:
        sqlite3.connect('books.db')
        logging.info('Conexión exitosa.')
    except:
        logging.warning('conexion fallida')

conexion=connect()

def view():
    conexion
    cur =conexion.cursor()
    cur.execute("SELECT*  FROM books")
    rows = cur.fetchall()
    books=[]
    for i in rows:
        book = Book(i[0], True if i[1] == 1 else False, i[2], i[3])
        books.append(book)
    conexion.close()
    return books

lisbros=view()