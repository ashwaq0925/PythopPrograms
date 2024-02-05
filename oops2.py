class Sim:
    def connect(self):
        print("connect to network")


class Mobile:
    def __init__(self,s):
        self.s=s
        self.s.connect()

jio1=Sim()
airtel1=Sim()
apple1=Mobile(jio1)
apple2=Mobile(airtel1)
