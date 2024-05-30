dobasok=[3,1,1,2,1,5,5,4,4,4]
eredmenyek=[0]
letra=0

for i in dobasok:
    uj=eredmenyek[-1]+i
    if uj%10==0:
        uj=uj-3
        letra=letra+1
        eredmenyek.append(uj)
    else:
        eredmenyek.append(uj)

print("2. feladat")
print(*eredmenyek)
print("3. feladat")
print("A jaték során {} alkalommal lépett létrára".format(letra))
print("4. feladat")
if eredmenyek[-1]>=45:
    print("A játékos befejezte.")
else:
    print("A játékot abbahagyta.")

szamocskak=[0,10,2,45,6,7,8,9,10,107]
if max(szamocskak)%2==0:
    print("bence most is egy gonosz lelekéééééééé")
else:
    print("bence egy gonosz lelekéééééééééé")

#elseelse:
print("bence gonoszkodik allandoan")
