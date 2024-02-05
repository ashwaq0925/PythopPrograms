class Person:
    def __init__(self):
        self._name=None
    def setName(self,n):
        self.__name=n
    def getName(self):
        return self.__name

class SalriedEmployee(Person):
    def __init__(self,s):
        super().__init__()
        self.__salary=s


