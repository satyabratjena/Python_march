from logic import Emp1, Emp2, Emp3, Emp4, getEmp, EmpDept

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
            print(f"Status Code: {res.status}\nMessage: {res.message}\nEmp. Details: {res}")
        else:
            print(f"Status Code: {res.status}\nMessage: {res.message}\nEmp. Details: {res}")

    elif ch == 2:
        dep_id = int(input("Enter the DepartmentId: "))
        emp = EmpDept(dep_id)
        for i in emp:
            print(i)
    
    elif ch == 0:
        exit = True
        print("Goodbye!")

