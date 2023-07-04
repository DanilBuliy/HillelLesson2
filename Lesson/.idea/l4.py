stroka=input("Введите два слова через кому: ")
spl=stroka.replace(" ","").split(",")

a=spl[0] #1 слово
print(a)

b=spl[1] #2 слово
print(b)
#форматирование
formatted1="!%s %s?" % (a[::-1].upper(), b[::-1].capitalize())
print(formatted1)

formatted2="!{},{}?".format(a[::-1].upper(), b[::-1].capitalize() )
print(formatted2)

formatted3=(f"!{a[::-1].upper()},{b[::-1].capitalize()}?")
print(formatted3)

#общий вывод
print(stroka, formatted1, formatted2, formatted3,sep="<<<>>>")

#запись в файл
file = open("hillel.txt", "w", encoding="utf-8")
print(stroka, formatted1, formatted2, formatted3,sep="<<<>>>",file=file)
file.close()
file2 = open("hillel.txt", "r", encoding="utf-8")
print(file2.readlines())
file2.close()