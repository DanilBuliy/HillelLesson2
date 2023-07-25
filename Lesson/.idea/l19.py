import csv
import openpyxl
book=openpyxl.Workbook()
sheet1=book.active

with open("dict1.csv", "r", encoding="utf-8") as f:
    obj=csv.reader(f)
    for i in obj:
        if i:
            print(i[0],i[1],i[3])
            sheet1.append([i[0],i[1],i[3]])
book.save("book.xlsx")
book.close()
