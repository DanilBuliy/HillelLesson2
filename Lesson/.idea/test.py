def dec_1(n):
    def decor(f):
        def obert(name):
            for i in range(n):
                print(f'Hi to {name}',end=' ')
            f(name)

        return obert
    return decor

@dec_1(3)
def c(name):
    print(f'{name}')

c('danilo')


