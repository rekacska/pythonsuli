#használt listák
Jatekok=["5ös lottó","6os lottó","skandináv","totó"]
#randomlist klónok hogy a lista definiálva legyen
randomlist = []
randomlist2 = []
randomlist3 = []

print("|=========================Választások=========================|")

for i, elem in enumerate(Jatekok):
    print("\t"+str(i+1)+":", elem)

print("\t0: Kilépés")
JatekId="alma"
while JatekId=="alma" or JatekId not in range(len(Jatekok)+1):
    try:
        JatekId=int(input("Válassz!"))
        if JatekId not in range(len(Jatekok)+1):
            raise 
    except:
        print("válassz a listából!")
print("|=========================Eredmény=========================|")

if JatekId==1:
    import random
    randomlist = []
    while len(randomlist)<5:
        n = random.randint(1, 91)
        if n not in randomlist:
            randomlist.append(n)
if len(randomlist)==5:
    print(randomlist)

if JatekId==2:
    import random
    randomlist2 = []
    while len(randomlist2)<6:
        n = random.randint(1,46)
        if n not in randomlist2:
            randomlist2.append(n)
if len(randomlist2)==6:
     print(randomlist2)

if JatekId==3:
    import random
    randomlist3 = []
    while len(randomlist3)<7:
        n = random.randint(1,36)
        if n not in randomlist3:
            randomlist3.append(n)
if len(randomlist3)==6:
     print(randomlist3)

if JatekId==4:
    import random
    Szavazatok= ["1","2","x"]
    randomlist4 = []
    while len(randomlist4)<14:
       randomlist4.append(random.choice(Szavazatok)) 
       
if len(randomlist4)==14:
    for i, elem in enumerate(randomlist4):
        print("\t"+str(i+1)+".mérközés:", elem)
    




