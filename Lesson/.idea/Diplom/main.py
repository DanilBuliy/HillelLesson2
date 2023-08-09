from vvodappend import *
from vuvod import *
from search import *
from savetojson import *
from readjson import *

def main():
    while True:
        print("1. Ввести новую запись (очищается БД)")
        print("2. Сделать дозапись")
        print("3. Поиск данных")
        print("4. Загрузить данные из ексель-бд")
        print("5. Экспортировать данные в json формат")
        print("6. Считать данные с json-файла")
        print('-' * 50)
        print("0. Выход")
        choice = input("Ваш выбор: ")

        if not choice.isdigit() or int(choice) > 6:
            print('-' * 50)
            print("Не корректный ввод")
            print('-' * 50)
            continue
        elif int(choice) == 1:
            print('-' * 50)
            vvod()
        elif int(choice) == 2:
            print('-' * 50)
            vvod2()

        elif int(choice) == 3:
            print('-' * 50)
            searchfunc()
            print('-' * 50)
        elif int(choice) == 4:
            print('-' * 50)
            vuvod()
        elif int(choice) == 5:
            print('-' * 50)
            savetojson()
        elif int(choice) == 6:
            print('-' * 50)
            readjson()
        elif int(choice) == 0:
            break


if __name__ == "__main__":
    main()
