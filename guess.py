import random

nummer=random.randint(1,100)

#print(nummer)

count=0;
while True:
    count = count + 1
    inv=int(input("getal "))
    if inv>nummer:print("lager")
    if inv < nummer:print("hoger")
    if inv==nummer:
        print("bingo pogingen "+str(count))
        break

