Jatekok=["5ös lottó","6os lottó","skandináv","totó"]

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

if JatekId==2:
    import random
    randomlist2 = []
    while len(randomlist)<6:
        n = random.randint(1,46)
        if n not in randomlist2:
            randomlist2.append(n)
            print(randomlist2)

if JatekId==1:
    import random
    randomlist = []
    while len(randomlist)<5:
        n = random.randint(1, 91)
        if n not in randomlist:
            randomlist.append(n)
            print(randomlist)


