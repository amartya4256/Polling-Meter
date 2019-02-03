import sqlite3
from config import *
from flask_login import current_user
import time

db="poll_database.db"

def connect():
    conn=sqlite3.connect(db,check_same_thread=False)
    return conn

def create_poll_table(var,c):
    code = "CREATE TABLE IF NOT EXISTS "+var+"(name VARCHAR(50) NOT NULL, count INTEGER NOT NULL DEFAULT 0)"
    #print(code)
    c.execute(code)

def create_option(c,option,var):
    code="INSERT INTO "+var+"(name) VALUES (?)"
    #print(code)
    c.execute(code,(option))

def update_vote(conn,c,option,var):
    conn=sqlite3.connect("poll_database.db")
    c=conn.cursor()
    code = "UPDATE "+var+" SET count=count+1 WHERE name=?"
    print(code)
    c.execute(code,(option,))
    save = "UPDATE user SET voted=1 WHERE id = ?"
    print(current_user.id)
    c.execute(save,(current_user.id,))
    conn.commit()

def clear_otp(conn, c, table, x):
    conn=sqlite3.connect("poll_database.db")
    c=conn.cursor()
    code = "UPDATE " + table + " SET otp = '' WHERE id = ?"
    c.execute(code, (x,))
    conn.commit()

def func1(conn,c,value):
    time.sleep(120)
    clear_otp(conn, c, "user", value)


def find_user(uid):
    c=connect().cursor()

    c.execute("SELECT otp FROM user WHERE id=(?)",(uid,))
    a=c.fetchone()
    if (a==None):
        return 0
    else:
        return a[0]

def user_login(c,uid):
    c.execute("SELECT * FROM user WHERE id=(?)",(uid,))
    return c.fetchone()

def main():
    db="poll_database.db"
    conn=connect(db)
    c=conn.cursor()

    var=input("ENTER POLL NAME : ")
    create_poll_table(var,c)
    option=input("ENTER OPTIONS USING COMMAS : ")
    option=option.split(",")
    for i in range(0,len(option)):
        #print(option[i])
        create_option(c,option[i],var)
    print("Connection Estabilished")
    conn.commit()
if __name__ == '__main__':
    main()