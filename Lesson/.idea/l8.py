import random
def choose(a):

    r = random.randint(1,3)

    if int(a) == r:
        print("Вы угадали!!!")
    else:
        print("Повезет в другой раз ({})".format(r))



while True:
    a = (input("Угадайте какое число я загадал \n"
               "Введите число от 1 до 3: "))
    if a.isdigit():
        choose(a)
        break
    else:
        print("это не число")
        continue

