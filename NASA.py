f=open("NASAlog.txt")
adatok=[]

for sor in f:
    adatok.append(sor.split("*"))


f.close()
print(adatok)