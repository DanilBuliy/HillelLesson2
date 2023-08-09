import json
import openpyxl

def savetojson():
    try:
        file_path = "data.xlsx"
        data = []
        workbook = openpyxl.load_workbook(file_path)
        sheet1 = workbook.active
        data = list(sheet1.values)
        with open("dipl.json","w",encoding="utf-8") as f:
            json.dump(data,f,indent=3,ensure_ascii=False)
        print("Запись в json-файл СДЕЛАНА!!!")
        print("-"*50)
    except FileNotFoundError:
        print("Такого файла нет")