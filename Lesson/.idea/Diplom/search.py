import openpyxl


def searchfunc():
    file_path = "data.xlsx"
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet1 = workbook.active
        data = list(sheet1.values)

        for row in data:
            print(*row)

        print("-" * 50)
        while True:
            search = input("Введите данные о записи, которую ищите: ")
            found = False

            add = ["Пол", "Имя", "Фамилия", "Отчество", "Дата рождения", "Дата смерти"]
            print(*add)
            for row in data[1:]:
                for cell_value in row:
                    if search.lower() in str(cell_value).lower():
                        print(*row)
                        found = True
                        break



            if not found:
                print("Запись не найдена")

            if  found == True or found != True:
                st = input("Повторить поиск (Y), завершить - любая клавиша: ")
                if "Y".lower() in st.lower():
                    continue
                else:
                    break

    except FileNotFoundError:
        print("Нет такого файла")
        print("-"*50)


