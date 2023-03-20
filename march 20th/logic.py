from model import Employee, EmpStatus

Emp1= Employee(1,"Ramesh", "A +ve", 101)
Emp2= Employee(2,"Sunil","B +ve", 102)
Emp3= Employee(3, "Eren", "AB -ve", 101)
Emp4= Employee(4, "Satya", "B +ve", 102)
Emp5= Employee(4, "Aakash", "AB -ve", 103)


empty = {Emp1.EmpNo:Emp1,Emp2.EmpNo:Emp2,Emp3.EmpNo:Emp3,Emp4.EmpNo:Emp4,Emp5.EmpNo:Emp5}

def getEmp(i):
    try:
        return empty[i]
    except:
        return "No such Employee ID"

def EmpDept(i):
    l = []
    for j in empty.values():
        if j.department_id == i:
            l.append(j.name)
        return l
