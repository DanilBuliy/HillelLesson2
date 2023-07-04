while(True):
    name=input("Введите имя-> ")
    age=input("Введите свой возраст-> ")
    if not age.isdigit() or int(age)<=0:
            print("Ошибка, повторите ввод")
    elif 0<int(age)<10:
        print(f"Привет, шкет #{name}#")
    elif 10<=int(age)<=18:
        print("Как жизнь #%s#?"%(name))
    elif 18 < int(age) < 100:
        print("Что желаете #{}#?".format(name))
    else:
        print(f"#{name}#, вы лжете - в наше время столько не живут...")
    res=input("Желаете выйти? (Д/Y)")
    #if res=="Д" or res=="Д".lower():
    if res.upper()=="Д" or res.upper()=="Y":
        break
    #elif res=="Y" or res=="Y".lower():
        #continue
    else:
        print("непонятный текст")
