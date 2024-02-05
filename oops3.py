class Person:
    class Address:
        def __init__(self):
            self.__street=None
            self.__city=None
        def read_address(self):
            self.__street=input("enter street")
            self.__city=input("enter city")
        def print_address(self):
            print(f'stree{self.__street}')
            print(f'city{self.__city}')

        def read_person(self):
            


