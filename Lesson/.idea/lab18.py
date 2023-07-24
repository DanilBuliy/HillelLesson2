import json
import csv
import random


with open("dict1.json", "r") as f:
    data = json.load(f)

with open("dict1.csv", "w", encoding="utf-8") as f1:
    wr = csv.writer(f1)
    wr.writerow(["ID", "Имя", "Возраст", "Телефон"])

    pre = ["095", "066", "098", "096", "050", "097"]
    numb = [random.randint(900000, 10000000) for i in range(len(data))]

    for i, y in data.items():
        wr.writerow([i, *y, f"{pre[random.randint(1, len(pre)+1)]}{numb.pop()}"])

