import sqlite3, random, datetime
from models import Book

def getNewId():
    return random.getrandbits(28)


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

def connect():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, available BOOLEAN, title TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()
    
    for i in books:
        bk=Book(getNewId(), i['available'], i['title'], i['timestamp'])
        insert(bk)