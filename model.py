import sqlite3 as sql

def insertUser(email, password):
    con = sql.connect("shoutout.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    con.commit()
    con.close()

def getUser():
    con = sql.connect("shoutout.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    con.close()
    return users