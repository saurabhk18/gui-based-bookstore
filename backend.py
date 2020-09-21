import sqlite3 as sql

def connect():
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn)) # NULL is used for id field which will auto-increment. So you don't have to pass 0, 1, 2 etc.
    conn.commit()
    conn.close()

def view():
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book") # NULL is used for id field which will auto-increment. So you don't have to pass 0, 1, 2 etc.
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""): # user may enter text in one or more fields. For query to run if only some field values are passed, it needs default values
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id): # user may enter text in one or more fields. For query to run if only some field values are passed, it needs default values
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sql.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()

#update(11,"Tender is the Night", "Fitzgerald", 1934, 22288098)
#delete(6)
#print("After deletion: ",view())
#print(search(author="John Doe"))
#update(2,"The Nightmare","Jane Doe",1919, 1000999)
#print(view())

