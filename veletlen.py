import random
import math

def veletlen(mettol, meddig, lepes=1):
    darab=math.ceil((meddig-mettol)/lepes)
    eltolas=mettol

    szam=math.floor(random.random()*darab)*lepes+eltolas
    return szam 

veletlen(10,20)
print(veletlen(10,20))
szamok=[]
for i in range(100):
    szamok.append(veletlen(10,20))
print(szamok)

veletlen(10,20)
#print(veletlen(10,20))
magassag=[]
r=veletlen(10,20)
for _ in range(r):
    r2=veletlen(10,21)
    temp=[]
    for _ in range(r2):
        temp.append(veletlen(160,201))
    magassag.append(temp)

#print(szamok)

szamok=[[veletlen(160,200)for _ in range(veletlen(10,21))]for _ in range(veletlen(10,20))]
print(magassag)
szamok=[[veletlen(160,201) for _ in range(veletlen(10,20))]for _ in range(veletlen(10,20))]
