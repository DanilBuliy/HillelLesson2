inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

inputdata2=list(filter(lambda x:x if x[::-1].lower()==x.lower() else "",inputdata))
print(inputdata2)

