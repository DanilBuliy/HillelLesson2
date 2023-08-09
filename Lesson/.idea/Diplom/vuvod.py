import openpyxl
import json


def vuvod():
    file_path = "data.xlsx"
    data = []
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet1 = workbook.active
        data = list(sheet1.values)
        for i in data:
            print(*i)
    except FileNotFoundError:
        print("Нет такого файла")
    print("-" * 50)
    return data








