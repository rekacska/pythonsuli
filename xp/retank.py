import math
import random

def veletlen(mettol,meddig,lepes=1):
    darab=math.ceil((meddig-mettol)/lepes)
    eltolas=mettol
    
    szam=math.floor(random.random()*darab)*lepes+eltolas
    return szam
tippszam=1
tankHelye=[]

while len(tankHelye)<2:
    tankHelye.append(veletlen(1,16))

playerVizszint=input("add meg a tank vizszintes helyét: ")
playerFuggoleges=input("add meg a tank függőleges helyét: ")

while True:
    if int(playerVizszint)==tankHelye[0] and int(playerFuggoleges)==tankHelye[1]:
        print("nyertél")
        print("Ennyiszer tippeltél: "+str(tippszam))
        break
    else: 
        print("ilyen messze vagy vizszinten: "+str(abs(int(playerVizszint)-tankHelye[0]))+" ilyen messze vagy fuggolegesen: "+str(abs(int(playerFuggoleges)-tankHelye[1])))
        tippszam+=1
        playerVizszint=input("add meg a tank vizszintes helyét: ")
        playerFuggoleges=input("add meg a tank függőleges helyét: ")
