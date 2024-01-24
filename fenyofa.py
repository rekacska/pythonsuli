<<<<<<< HEAD
from tkinter import *
import math
import random

=======
>>>>>>> a21e2210f99e27c965e55a780525753aed7c66f9
def eltol(pontok,x,y):
    for i in range(0,len(pontok),2):
        pontok[i]+=x
        pontok[i+1]+=y
    return pontok
<<<<<<< HEAD

def nagyit(pontok,x,y=-1):

    if y==-1:
        print(y)
        for i in range(len(pontok)):
            pontok[i]*=x
    else:
        for i in range(len(pontok)):
            if i%2==0:
                pontok[i]*=x
            else:
                pontok[i]*=y

    return pontok

#x'
#y'
def fogatpont(x,y,szog):
    x2=math.cos(math.radians(szog))*x - math.sin(math.radians(szog))*y
    y2=math.cos(math.radians(szog))*x + math.cos(math.radians(szog))*y

    return x2,y2

def forgat(lista,szog,ox=0,oy=0):

    lista=eltol(lista,-oX,-oY)

    for i in range(0,len(lista),2):
        lista[i],lista[i+1]=forgatPont(lista[i],lista[1+1],szog)

        return lista
    
def forgatPontKorul(lista,)

def faSorsol(darab):
    lista=[]

    temp=[]
    temp.append(random.randint(0,1))
    temp.append(random.randint(0,600))
    temp.append(random.randint(0,600))
    temp.append(random.randint(20,30)/100)
    




    return lista

win=Tk()

win.geometry("600x600")

canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightpink")
canvas.pack(fill = BOTH, expand = 1)

pontok=[0,0,100,0,100,100,0,100]

#eltolás
=======
from tkinter import *
import math

win=Tk()
win.geometry("600x600")

canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightblue")
canvas.pack(fill=BOTH,expand=1)

pontok=[0,0,100,0,100,100,0,100,0,0]
canvas.create_line(pontok,width=1.5,fill="green")
>>>>>>> a21e2210f99e27c965e55a780525753aed7c66f9
for i in range(0,len(pontok),2):
    pontok[i]+=200
    pontok[i+1]+=100

<<<<<<< HEAD
canvas.create_line(pontok,width=5,fill="purple")
pontok=eltol(pontok,100,0)
print(pontok)
canvas.create_line(pontok,width=5,fill="purple")


fenyo1=[200,0,0,400,190,400,190,500,210,500,210,400,400,400,200,0]
pontok=eltol(fenyo1,10,10)
canvas.create_line(fenyo1,width=5,fill="green")
fenyo2=[200,0,
        0,100,
        150,100,
        0,200,
        150,200,
        0,300,
        150,300,
        150,400,
        250,400,
        250,300,
        400,300,
        250,200,
        400,200,
        250,100,
        400,100,
        200,0]

fenyo2=eltol(fenyo2,200,200)
fenyo2=nagyit(fenyo2,0.5,1)
fenyo2=forgat(fenyo,90)

canvas.create_line(fenyo2,width=5,fill="green")

win.mainloop()

=======

canvas.create_line(pontok,width=1.5,fill="green")
pontok=eltol(pontok,0,100)

win.mainloop()

fenyo1=[200,0,0,400,190,400,190500,210,500,210,400,400,400,200,0]
>>>>>>> a21e2210f99e27c965e55a780525753aed7c66f9
