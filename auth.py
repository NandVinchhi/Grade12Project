import mysql.connector as sqltor
from random import choice

def createid():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    final = ""

    for i in range(8):
        final += choice(chars)
    return final

def sqlconnect():
    conn = sqltor.connect(host='localhost', user='root', passwd='mysql123', database='grade12project')
    return conn

def studentlogin():
    conn = sqlconnect()
    cursor = conn.cursor()
    email = input("Enter email: ")
    passwd = input("Enter password: ")
    cursor.execute(f"select * from student where email='{email}';")
    l = cursor.fetchall()

    if len(l) == 0:
        print("No user found.")
        return ""
    else:
        if l[0][3] == passwd:
            print("Logged in successfully!")
            return l[0][0]
        else:
            print("Incorrect email or password.")
            return ""

def teacherlogin():
    conn = sqlconnect()
    cursor = conn.cursor()
    email = input("Enter email: ")
    passwd = input("Enter password: ")
    cursor.execute(f"select * from teacher where email='{email}';")
    l = cursor.fetchall()

    if len(l) == 0:
        print("No user found.")
        return ""
    else:
        if l[0][3] == passwd:
            print("Logged in successfully!")
            return l[0][0]
        else:
            print("Incorrect email or password.")
            return ""

def studentsignup():
    conn = sqlconnect()
    cursor = conn.cursor()
    email = input("Enter email: ")
    passwd = input("Enter password (min 8 chars): ")
    studentname = input("Enter student name: ")
    classsec = input("Enter class and section (eg. 12A): ")
    school = input("Enter school: ")

    cursor.execute(f"select * from student where email='{email}';")
    l = cursor.fetchall()
    

    if len(l) > 0:
        print("This user already exists. Please login.")

    elif len(passwd) < 8:
        print("Password needs to be atleast 8 characters long.")
    else:
        userid = createid()
        cursor.execute(f"insert into student values ('{userid}', '{email}', '{studentname}', '{passwd}', '{classsec}', '{school}');")
        conn.commit()
        print("Signed up successfully!")

def teachersignup():
    conn = sqlconnect()
    cursor = conn.cursor()
    email = input("Enter email: ")
    passwd = input("Enter password (min 8 chars): ")
    teachername = input("Enter teacher name: ")
    school = input("Enter school: ")

    cursor.execute(f"select * from teacher where email='{email}';")
    l = cursor.fetchall()

    if len(l) > 0:
        print("This user already exists. Please login.")

    elif len(passwd) < 8:
        print("Password needs to be atleast 8 characters long.")
    else:
        userid = createid()
        cursor.execute(f"insert into teacher values ('{userid}', '{teachername}', '{email}', '{passwd}', '{school}');")
        conn.commit()
        print("Signed up successfully!")