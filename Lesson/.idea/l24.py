import math

class Calc:
    def __init__(self, numb1, numb2=None):
        self.numb1 = numb1
        self.numb2 = numb2

    def decor(p):
        def func(self):
            print("-" * 20)
            result = p(self)
            print("-" * 20)
            return result
        return func

    @property
    @decor
    def sum(self):
        print("ДОБАВЛЕНИЕ")
        #if self.numb2<0:
            #raise ValueError("Второй елемент должен быть > 0")
        if self.numb2 < 0:
            raise ValueError("Второй элемент должен быть >= 0")
        res=self.numb1 + self.numb2
        return res

        #return f"Результат: {self.numb1 + self.numb2}"

    @property
    @decor
    def minus(self):
        print("ОТНИМАНИЕ")
        try:
            res=self.numb1 - self.numb2
            return f"Результат: {res}"
        except Exception as e:
            return f"Ошибка: {e}"

    @property
    @decor
    def delit(self):
        print("ДЕЛЕНИЕ")
        try:
            res = round(self.numb1 / self.numb2)
            return f"Результат: {res}"
        except ZeroDivisionError:
            return "Нельзя на 0 делить"

    @property
    @decor
    def umnozh(self):
        print("УМНОЖЕНИЕ")
        try:
            res=self.numb1 * self.numb2
            return f"Результат: {res}"
        except Exception as e:
            return f"Ошибка: {e}"

    @property
    @decor
    def stepen(self):
        print("ВОЗВЕДЕНИЕ В СТЕПЕНЬ")
        if self.numb2<0:
            raise ValueError("Степень должна быть > 0")
        return f"Результат: {self.numb1 ** self.numb2}"

    @property
    @decor
    def sqrt(self):
        print("ИЗВЛЕЧЕНИЕ КВАДРАТНОГО КОРНЯ")

        try:
            if self.numb1 < 0:
                raise ValueError("Извлечение корня из отрицательного числа недопустимо.")
            res = math.sqrt(self.numb1)
            return res
        except ValueError as error:
            return f"Ошибка: {error}"
        except Exception as e:
            return f"Ошибка: {error}"



while True:
    number1 = input("Введите число: ")
    if number1.isdigit() or number1.startswith("-") and number1[1].isdigit():
        while True:
            st = input("Выберите операнд:\n"
                       "+ - 1\n"
                       "- - 2\n"
                       "/ - 3 \n"
                       "* - 4\n"
                       "^(возведение в степень) - 5\n"
                       "sqrt(извлечение квадр. корня) - 6 \n"
                       "------------ \n"
                       "Ввод: ")
            if st in ("1", "2", "3", "4", "5", "6") or st in ("+", "-", "/", "^", "sqrt"):
                break
            else:
                print("Нет такого пункта")
        break
    else:
        print("Просили ввести число!!!")

if st in ("sqrt", "6"):
    obj = Calc(int(number1))
    print(obj.sqrt)
else:
    while True:
        number2 = input("Введите 2-е число: ")
        if number2.isdigit() or number2.startswith("-") and number2[1].isdigit():
            obj1 = Calc(int(number1), int(number2))
            break
        else:
            print("Просили ввести число!!!")

    if st in ("+", "1"):
        print(obj1.sum)
    elif st in ("-", "2"):
        print(obj1.minus)
    elif st in ("/", "3"):
        print(obj1.delit)
    elif st in ("*", "4"):
        print(obj1.umnozh)
    elif st in ("^", "5"):
        print(obj1.stepen)

