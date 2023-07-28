class String(str):

    def __add__(self, other):
        result=str(self)+str(other)
        print(result)
        return result


    def __sub__(self, other):
        res=self.replace(str(other), '')
        print(res)
        return res

String('New') + String(890)
String(1234) + 5678
String('New') + 'castle'
String('New') + 77
String('New') + True
String('New') + ['s', ' ', 23]
String('New') + None

print("-"*50)

String('New bala7nce') - 7
String('New balance') - 'bal'
String('New balance') - 'Bal'
String('pineapple apple pine') - 'apple'
String('New balance') - 'apple'
String('NoneType') - None
String(55678345672) - 7

