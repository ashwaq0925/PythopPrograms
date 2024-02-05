class A:
    def m1(self):
        print("m1 of A class")
    def m2(self):
        print("m2 of A class")
class B(A):
    def m3(self):
        print("m3 of B class")


objb=B()
objb.m1()
objb.m2()
objb.m3()