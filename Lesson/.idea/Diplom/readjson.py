import json

def readjson():
    try:
        with open("dipl.json","r",encoding="utf-8") as f:
            jsdata = json.load(f)
            for i in jsdata:
                print(*i)
            print("-"*50)
    except:
        print("Такого файла нет!")
