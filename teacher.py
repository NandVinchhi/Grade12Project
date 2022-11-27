import mysql.connector as sqltor
from random import choice
from tabulate import tabulate

def sqlconnect():
    conn = sqltor.connect(host='localhost', user='root', passwd='mysql123', database='grade12project')
    return conn


def createid():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    final = ""

    for i in range(8):
        final += choice(chars)
    return final

def createclass(userid):
	conn = sqlconnect()
	cursor = conn.cursor()

	classid = createid()

	classname = input("Enter class name: ")


	cursor.execute(f"insert into class values ('{classid}', '{classname}');")
	cursor.execute(f"insert into teachermembership values ('{classid}', '{userid}');")
	
	conn.commit()

def manageclasses(userid):
	conn = sqlconnect()
	cursor = conn.cursor()

	cursor.execute(f"select (classid, classname) from teachermembership, class where teachermembership.classid = class.classid and teachermembership.teacherid = '{userid}';")
	l = cursor.fetchall()
	print("Your classes:")
	print(tabulate(l, ["Class ID", "Class Name"], tablefmt="pretty"))

def viewassignments():
	conn = sqlconnect()
	cursor = conn.cursor()
	classid = input("Enter Class ID: ")
	cursor.execute(f"select * from assignment where classid= '{classid}';")
	l = cursor.fetchall()
	print("Your assignments:")
	print(tabulate(l, ["Assignment ID", "Class ID", "Assignment Name", "Deadline"], tablefmt="pretty"))

def viewproblem():
	conn = sqlconnect()
	cursor = conn.cursor()
	assignmentid = input("Enter Assignment ID: ")
	cursor.execute(f"select problemid from problem where assignmentid= '{assignmentid}';")
	l = cursor.fetchall()
	print("Problems in this assignment:")
	print(tabulate(l, ["Problem ID"], tablefmt="pretty"))
	problemid = input("Enter Problem ID: ")

	cursor.execute(f"select problem from problem where problemid= '{problemid}';")
	l = cursor.fetchall()

	if len(l) == 0:
		print("Invalid ID.")
	else:
		print(l[0][2])

def viewsubmission(userid):
	conn = sqlconnect()
	cursor = conn.cursor()
	assignmentid = input("Enter Assignment ID: ")
	cursor.execute(f"select problemid from problem where assignmentid= '{assignmentid}';")
	l = cursor.fetchall()
	print("Problems in this assignment:")
	print(tabulate(l, ["Problem ID"], tablefmt="pretty"))
	problemid = input("Enter Problem ID: ")

	print("Submissions:")

	cursor.execute(f"select submissionid, complete from submission where problemid= '{problemid}';")
	l = cursor.fetchall()
	print(tabulate(l, ["Submission ID", "Completed (0/1)"], tablefmt="pretty"))

	subid = input("Enter Submission ID:")

	cursor.execute(f"select code, comments from submission where submissionid= '{subid}';")
	l = cursor.fetchall()

	print(l[0][0])

	print("Teacher's comments:")

	print(l[0][1])