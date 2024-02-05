class A:
    def __init__(self):
        self.x=100
        self.y=200


class B(A):
    def __init__(self):
        super().__init__()
        self.p=300
        self.q=400



objb=B()
print(objb.p,objb.q)
print(objb.x,objb.y)