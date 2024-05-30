from ALeghosszabbJátszmaClass import *
f=open("labdamenetek5.txt")
eredmenyek=[]
for sor in f:
    eredmenyek.append(LabdaMenet(sor))

f.close()
AVagyF=len(eredmenyek)
print("3. feladat: Labdamenetek száma: {}".format(AVagyF))

#(adogato jatekos nyeresei/labdamenetek szama)*100

adogatoJatekos=0
for jatekos in eredmenyek:
    if jatekos.jatekos[0]=="A":
        adogatoJatekos+=1
print(adogatoJatekos)
nyeresekSzazaleka=(adogatoJatekos/AVagyF)*100
print("Az adogató jatékos {}-ban nyerte meg a labdamenetet".format(nyeresekSzazaleka))

leghoszabbAdogatas=0
eppeniAdogatas=0
for jatekos in eredmenyek:
    if jatekos.jatekos[0]=="A":
        eppeniAdogatas+=1
    else:
        if leghoszabbAdogatas<eppeniAdogatas:
            leghoszabbAdogatas=eppeniAdogatas
        eppeniAdogatas=0
print("A leghosszabb sorozat: {}".format(leghoszabbAdogatas))

#A A F A F A A F
#2 1 2