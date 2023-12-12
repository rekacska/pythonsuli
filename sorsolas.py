import random

nevDb=100

vNev=("Nagy","Kis","Horváth","Kovács","Bogdán","Lakatos","Fazekas")
kNev=(
("Bikárdó","Leonidász","Naruto","Béla","Pista","Rozalinda")
("Marika","Piroska","Aranka","Britni")
)

nevLista=[]
nem=range.randrange(2)
tempNev=random.choice(vNev)+" "+random.choice(kNev[nem])
if random.randrage(0,3)==0:
    tempNev+=" "+random.choice(kNev[nem])


nevLista.append(tempNev)


print(nevLista)
