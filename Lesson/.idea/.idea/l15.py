a=input("Введите строку №1: ")
b=input("Введите строку №2: ")
c=input("Введите строку №3: ")
d=input("Введите строку №4: ")

f=open("newfile.txt","w", encoding="utf-8")
f.write(a+"\n")
f.write(b+"\n")
f.close()


f=open("newfile.txt","a",encoding="utf-8")
f.write(c+"\n")
f.write(d+"\n")
f.close()