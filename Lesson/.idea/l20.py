class Auto:

    def __init__(self,brand,mark,age,color="black",weight="2.5t"):
        self.brand=brand
        self.mark=mark
        self.age=age
        self.color=color
        self.weight=weight
    def move(self):
        print("move")
    def stop(self):
        print("stop")
    def birthday(self):
        self.age+=1
        print(self.age)

o=Auto("Lux","Mercedes",age=34)
o.move()
o.stop()
o.birthday()


