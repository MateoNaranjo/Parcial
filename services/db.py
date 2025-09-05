import sqlite3, random, datetime
from models.Books import Book


books = [
    
    {
        'available':True,
        'title':'Don Quijote',
        'timestamp':datetime.datetime.now()
    },
    
    {
        'available':True,
        'title':'El principito',
        'timestamp':datetime.datetime.now()
    },
    
     {
        'available':True,
        'title':'Harry Potter y la camara de los secretos',
        'timestamp':datetime.datetime.now()
    },
      {
        'available':True,
        'title':'El Hobbit',
        'timestamp':datetime.datetime.now()
    },
]


def insert(book):
    try:
        conn=sqlite3.connect('books.db')
        cur=conn.cursor()
        cur.execute("INSERT INTO books VALUES (?,?,?,?)",(
            book.id,
            book.available,
            book.title,
            book.timestamp
        ))
        conn.commit()
        conn.close()
        return "Datos insertados correctamente"
    except:
        return "Error al insertar datos"
