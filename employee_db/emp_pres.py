from emp_logic import  getEmp, EmpDept
from emp_model import Employee, EmpStatus

def employee():
    exit = False

    while exit == False:
        print("** Main Menu **")
        print("1. Enter the EmpNo.")
        print("2. Enter the DepartmentId.")
        print("0. Exit")

        ch = int(input("Enter your choice: "))
        choice(ch)

def choice(ch):
    if ch == 1:
        emp_no = int(input("Enter the EmpNo: "))
        emp = getEmp(emp_no)
        if emp.status == 1:
            print(f"Status Code: {emp.status}\nMessage: {emp.message}\nEmployee Details: {emp.EmpObj}")
        else:
            print(f"Status Code: {emp.status}\nMessage: {emp.message}\nEmployee Details: {emp.EmpObj}")
        

    elif ch == 2:
        dep_id = int(input("Enter the DepartmentId: "))
        emp2 = EmpDept(dep_id)
        for i in emp2:
            print(i)

    elif ch == 3:
        emp_no = int(input("Enter the employee number: "))
        emp3 = EmpStatus(emp_no)
        if emp3.emp_status == 0:
            print("Employee number not found")
        else: 
            print(emp3.EmpObj)

    elif ch == 0:
        exit = True
        print("Goodbye!")

