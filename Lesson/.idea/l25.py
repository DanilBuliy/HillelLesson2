def generator(a):
    b1 = -2
    q = -5
    for i in range(a):
        yield b1
        b1*=q

a=generator(6)
for i in a:
    print(i)

print("-"*50)

def generator2(a):
    b1 = 10
    q = 3
    for i in range(a):
        yield b1
        b1*=q

a=generator2(6)
for i in a:
    print(i)

