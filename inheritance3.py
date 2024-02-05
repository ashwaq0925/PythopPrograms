class Person:
    def __init__(self):
        self.__name=None
    def setName(self,n):
        self.__name=n
    def getName(self):
        return self.__name


class Student(Person):
    def __init__(self):
        super(). __init__()
        self.__course=None
    def setCourse(self,c):
        self.__course=c
    def getCourse(self):
        return self.__course

stud1=Student()
stud1.setName("ashwaq")
stud1.setCourse("python")
print(f'Student Name {stud1.getName()}')
print(f'Student Course {stud1.getCourse()}')