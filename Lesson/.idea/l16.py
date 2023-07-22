s = b'r\xc3\xa9sum\xc3\xa9'
#декодируем в строку
a=s.decode()
print(a)
#кодируем в байтовый вид с Latin1-код.
c=a.encode('Latin1')
print(c)
#декодируем в строку Latin1-код
d=c.decode('Latin1')
print(d)