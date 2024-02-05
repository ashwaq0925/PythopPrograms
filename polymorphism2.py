class Employee:
    def __init__(self):
        self.__ename=None
        self.__job=None
    def read(self):
        self.__ename=input("enter Employee Name :  ")
        self.__job=input("enter employee job : ")
    def print_info(self):
        print(f'EmployeeName{self.__ename}')
        print(f'employeejob{self.__job}')
class SalariedEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.__salary=None

    def read(self):
        super().read()
        self.__salary=float(input("enter employee salary : "))
    def print_info(self):
        super().print_info()
        print(f'employee salary {self.__salary}')


emp1=SalariedEmployee()
emp1.read()
emp1.print_info()