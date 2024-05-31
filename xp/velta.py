import math
import random

def veletlen(mettol,meddig,lepes=1):
    darab=math.ceil((meddig-mettol)/lepes)
    eltolas=mettol

    szam=math.floor(random.random()*darab)*lepes+eltolas
    return szam

korSzama=1
gepszama=veletlen(1,16)
playerTipp=int(input("Add meg a tipped: "))

while korSzama!=3:
    if playerTipp==gepszama:
        print("Nyertél!")
        break
    else:
        print("Ilyen messze van a számod a gondolt számtól: "+str(abs(playerTipp-gepszama)))
        korSzama+=1
        playerTipp=int(input("Add meg a tipped: "))
    