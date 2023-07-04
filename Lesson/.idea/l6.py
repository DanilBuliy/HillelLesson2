
while True:
    n = input("Введите целое число: ")
    if not n.lstrip('-').isdigit():
        print("Это не число")
        continue
    elif int(n) <= 0:
        print("Вы ввели не положительное число")
        continue
    else:
        break

sum=0
n=int(n)
for i in range(1,n+1):
    i=i**3
    sum+=i
print("sum of cubs=",sum)



n = int(n)
sum=0
b=0
i = 1
while i <= n:
    b = i ** 3
    sum += b
    i += 1
print("sum через вайл=",sum)

