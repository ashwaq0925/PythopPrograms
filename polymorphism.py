class A:
    def m1(self):
        print("m1 of class A")
    def m2(self):
        print("m2 of class A")
class B(A):
    def m3(self):
        print("m3 of B class")
    def m1(self):
        super().m1()
        print("method overriding")


objb=B()
objb.m1()
objb.m2()
objb.m3()