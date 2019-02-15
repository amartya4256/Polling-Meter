import random
import sqlite3
import  way2sms
import app
import hashlib

def gen_otp():
    return str(random.randrange(100000,999999))

def save_otp(number,otp):
    conn=app.conn
    c = app.c
    save="UPDATE user SET otp=? where id=?"
    print(save)
    c.execute(save,(otp,number))
    conn.commit()


def send_otp(phnnumber,otp):
    way2sms.sendPostRequest(phnnumber,'your otp is '+ otp)

def otp_default(number,c,phn):
    x = gen_otp()
    y=x
    x = hashlib.md5(x.encode())
    x = str(x.hexdigest())
    save_otp(number,x)
    send_otp(phn,y)

def otp_test(number,c,phn):
    x = gen_otp()
    print(x)
    x = hashlib.md5(x.encode())
    x = str(x.hexdigest())
    print(type(x))
    print(x)
    save_otp(number,x)
    print(x)
    # send_otp(phn,x)