
adatok=[]
f=open("helsinki.txt")

for sor in f:
    adatok.append(sor.strip().split("\n"))
   
f.close()

for i in range(len(adatok)):
    adatok[i][0]=int(adatok[i][0])
    adatok[i][1]=int(adatok[i][1])
    adatok[i][2]=int(adatok[i][2])
    adatok[i][3]=int(adatok[i][3])
    temp=[]
    tempSor=sor.split(" ")
    for sor in tempSor:
        temp.append(sor.strip())

print(adatok)