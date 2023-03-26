from emp_db import *
from emp_model import *

def getEmp(i):
        message = getDeveloperInfo(i)
        if message != None:
            return EmpStatus(1,"Found",message)
        else:
            return None
        
def EmpDept(dept):
    dept_Id = getEmployeesByDeptId(dept)
    return dept_Id
