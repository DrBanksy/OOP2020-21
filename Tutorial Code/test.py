from collections import namedtuple

Person = namedtuple("Person", "age height weight")
jenny = Person("21", "120cm", "75kg")

concerts = {"longitude":(23, 45, 65), "Electric":(12,14,16)}

for values in concerts.values():
    print(values)
