inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

inputdata2=tuple(filter(lambda x:x if isinstance(x,str) and x[::-1].lower()==x.lower() else "",inputdata))
print(inputdata2)
