def rec(w: str):
    try:
        num = float(w.replace(",", "."))
        if w.isdigit() and int(w) > 0:
            s = "целое число"
        elif  w[0] == '-' and w[1:].isdigit():
            s = "отрицательное число"

        else:
            if num > 0:
                s = "дробное число"
            elif num < 0:
                s = "дробное отрицательное число"
            else:
                s = "Вы ввели ноль"
    except:
        s = f"Вы ввели некорректное число '{w}'"

    return s

while 1:
    word = input("Введите слово. (выход, exit, quit, e или q для выхода): ")
    if word.lower() in ["выход", "exit", "quit", "e", "q"]:
        print("Вы вышли из программы")
        break
    else:
        a = rec(word)
        print(a)
