import sqlite3

conn = None
try:
    conn = sqlite3.connect("E:/practice/movie.db")
    print("connection is secucessfully")
except sqlite3.DatabaseError as ex:
    print("error in connecting")
finally:
    if conn is not None:
        conn.close()
        print("dissconnect with db")
