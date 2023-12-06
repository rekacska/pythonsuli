def menu(lista):
    for i,elem in enumerate (lista):
        print("{}: {}".format(i+1,elem ))

    valasztas=0
    while valasztas<1 or valasztas>len(lista) and valasztas!=69:
        try:
            valasztas=int(input("válassz: "))
        except:
            pass

    return valasztas-1

lista =["előre", "hátra", "jobbra", "balra"]

#print("\n".join(lista))

#valasz=menu(lista)
#print(valasz,lista[valasz])

#nyelvválasztás
nyelvLista=["Magyar", "English","Deutsch","Russky"]
nyelvId={"Magyar":"szöveghun", "English":"szövegEng"}

print("válassz nyelvet!")

while True:
    nyelvValasztas=menu(nyelvLista)
    #print(nyelvLista[nyelvValasztas])
    if nyelvLista[nyelvValasztas] in nyelvId:
        break
    else:
        print("Sajnos ez a fordítás épp nem elérhető")
        
if nyelvId[nyelvLista[nyelvValasztas]]  == "szöveghun":
    import szöveghun as t
elif nyelvId[nyelvLista[nyelvValasztas]] == "szövegEng":
    import szövegEng

tortenet=[
        [
            1, #szál ID
            t.text["érkezés"],#szöveg
            ["fogmosás", "reggeli", "fölöltözés"], #valasztási lehetőségek
            [2,3,4] #hova ugorjon
        ],
        [
            2, #szál ID
            t.text["elmegyek fogat mosni. Sikálom rendesen, ahogy kell"],#szöveg
            ["fogmosás", "reggeli", "fölöltözés"], #valasztási lehetőségek
            [2,3,4] #hova ugorjon
        ],
        [
            3, #szál ID
            t.text["kellene valamit enni! Anya csinálsz valamit? Nézzük meg!"],#szöveg
            [t.text["fogmosás"], t.text["reggeli"], t.text["fölöltözés"]], #valasztási lehetőségek
            [2,3,4] #hova ugorjon
        ],
        [
            4, #szál ID
            t.text["kissé hűvös van, kellene valami ruha! \nFelveszek egy nadrágot, meg egy pólót"],#szöveg
            [t.text["fogmosás"], t.text["reggeli"], t.text["fölöltözés"], t.text["66-os parancs"]], #valasztási lehetőségek
            [2,3,4,66] #hova ugorjon
        ],
        [
            66, #szál ID
            t.text["végemindennek"],#szöveg
            [], #valasztási lehetőségek
            [] #hova ugorjon
        ]
         ]

szalID=1
while True:
    temp=[]
    for e in tortenet:
        temp.append(e[0])
    #másként
    temp=[e[0] for e in tortenet]
    szalIndex=temp.index(szalID)

    print(tortenet[szalIndex][1])
    
    if tortenet[szalIndex][2]==[]:
        break
    
    menuPont=menu(tortenet[szalIndex][2])
    
    if menuPont == 68:
        break

    szalID=tortenet[szalIndex][3][menuPont]

print("The End")


#print(tortenet[])





