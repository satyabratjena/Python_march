
class Employee:
    def __init__(self, EmpNo, name, BG, department_id):
        self.EmpNo = EmpNo
        self.name = name
        self.bg = BG
        self.department_id = department_id

    def __str__(self):
        return f"EmployeeId: {self.EmpNo}\nName: {self.name}\nBlood group: {self.BG}\nDept.Id {self.department_id}"

class EmpStatus():
    def __init__(self, status, message, EmpObj):
        self.status = status
        self.message = message
        self.EmpObj = EmpObj