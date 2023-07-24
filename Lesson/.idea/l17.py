dict1={
    123456:("John",30),
    123457:("Dan",20),
    123458:("Tom",44),
    123459:("Dima",33),
    123450:("Oleg",23),
    123451:("Sam",27)
}
print(dict1)

import json

f=open("dict1.json","w")
json.dump(dict1,f,indent=1)
f.close()