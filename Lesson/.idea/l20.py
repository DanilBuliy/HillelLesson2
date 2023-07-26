import time

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

class Truck(Auto):

    def __init__(self,max_load):
        self.maxl=max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):

    def __init__(self, max_speed):
        self.maxs = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.maxs}")
###Класс Трак####
obj=Truck(2000)
obj.move()
obj.load()

obj1=Truck(40000)
print("obj1 is",end=" ")
obj1.stop()
print("obj1 is",end=" ")
obj1.load()
###Класс Car#####
obj2=Car(400)
obj2.move()

obj3=Car(340)
obj3.move()