import time
from datetime import datetime
def v_decor(func):
    """Фун-я приветствия, добавляющая 'Hi, ' """
    def some(*args):
        print("Hi,",end=" ")
        a = datetime.now()
        func(*args)
        b = datetime.now()
        print(f"Время выполнения функции: {b - a}")
    return some


def n(name):
    print(f"{name}")
    time.sleep(0.5)
    print("Сейчас буду выдавать вам приз")
#1-ый способ декорирования
f=v_decor(n)

f("Evgeniy")
print("-"*100)

#2-ый способ декорирования
@v_decor
def count():
    a = {1: 'автомобиль', 2: 'вертолет', 3: 'F-16', 4: 'Яхта'}
    while True:
        choose = input(f"Выберите что-то одно {a}: ")
        for i, y in a.items():
            if choose.isdigit() and int(choose) == i or choose.lower() == y.lower():
                print(f"Вы получаете: {a[i]}")
                return choose
        print("Такого варианта нет =(")

count()
print("-"*105)


