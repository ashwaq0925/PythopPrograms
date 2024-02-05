class India:
    state="Telangana"
    place='godaverikhani'
    area= 'laxminagar'
country = India()
print(country.state)
print(country.place)
print(country.area)


print("==================================")

class Computer:
    def __init__(self,cpu ,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
         print("config is : " ,self.cpu,self.ram)

com1=Computer( 'i3',16)
com2=Computer("ryzen ",16)

com1.config()
com2.config()