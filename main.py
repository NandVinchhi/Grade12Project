import auth
import teacher
import student

loggedin = False
interface = 0
userid = ""
def welcome():
    with open("welcome.txt") as f:
        print(f.read())

def authenticate():
    global loggedin
    global interface
    global userid
    print("What would you like to do?")
    choice = int(input("""1. Student Login
2. Teacher Login
3. Create Student Account
4. Create Teacher Account
5. Quit
Enter choice (1-5): """))
    if choice == 1:
        userid = auth.studentlogin()

        if len(userid) > 0:
            loggedin = True
            interface = 1

    elif choice == 2:
        userid = auth.teacherlogin()

        if len(userid) > 0:
            loggedin = True
            interface = 2
    elif choice == 3:
        auth.studentsignup()
    elif choice == 4:
        auth.teachersignup()
    elif choice == 5:
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice.")
    print()

def studentinterface():
    global loggedin
    global interface
    global userid
    print("What would you like to do?")
    choice = int(input("""1. View Classes
2. View Assignments
3. View Problem
4. View Submission
5. Submit Code
6. Logout
7. Quit
Enter choice (1-7): """))
    if choice == 1:
        student.manageclasses(userid)
    elif choice == 2:
        student.viewassignments()
    elif choice == 3:
        student.viewproblem()
    elif choice == 4:
        student.viewsubmission(userid)
    elif choice == 5:
        student.submitcode()
    elif choice == 6:
        loggedin = False
        interface = 0
        userid = ""
        print("Logging out...")
    elif choice == 7:
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice.")
    print()

def teacherinterface():
    global loggedin
    global interface
    global userid
    print("What would you like to do?")
    choice = int(input("""1. Create Class
2. Manage Classes
3. View Students
4. View Assignments
5. View Problem
6. View Submission
7. Create Assignment
8. Logout
9. Quit:
Enter choice (1-9): """))
    if choice == 1:
        teacher.createclass(userid)
    elif choice == 2:
        teacher.manageclasses(userid)
    elif choice == 3:
        teacher.viewstudents()
    elif choice == 4:
        teacher.viewassignments()
    elif choice == 5:
        teacher.viewproblem()
    elif choice == 6:
        teacher.viewsubmission()
    elif choice == 7:
        teacher.createassignment()
    elif choice == 8:
        loggedin = False
        interface = 0
        userid = ""
        print("Logging out...")
    elif choice == 9:
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice.")
    print()

welcome()

while True:
    if loggedin:
        if interface == 1:
            studentinterface()
        elif interface == 2:
            teacherinterface()
    else:
        authenticate()