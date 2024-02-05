class engine:
    def start(self):
        print("engine start")
    def stop(self):
        print("engine stop")

class car:
    def __init__(self):
        self.e=engine()
    def start(self):
        self.e.start()

    def stop(self):
        self.e.stop()


car1=car()
car1.start()
car1.stop()
