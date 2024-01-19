from tkinter import *
import math

def eltol(pontok,x,y):
    for i in range(0,len(pontok),2):
        pontok[i]+=x
        pontok[i+1]+=y

    return pontok

def nagyit(pontok,x,y=True):
    if y==True:
        print(y)
        for i in range(len,(pontok)):
            pontok[i]*=x
        else:
            for i in range(len,(pontok)):
                if i%2==0:
                    pontok[i]*=x
                else:
                    pontok[i]*=y

    return pontok

def fasor(darab):
    lista=[]

    temp=[]
    temp.append(random.randint(0,1))
    temp.append(random.randint(0,600))
    temp.append(random.randint(0,600))
    temp.append(random.randint(20,30/100))

    return lista

win=Tk()

win.geometry("600x600")

canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightpink")
canvas.pack(fill = BOTH, expand = 1)

pontok=[0,0,100,0,100,100,0,100]

#eltolás
for i in range(0,len(pontok),2):
    pontok[i]+=200
    pontok[i+1]+=100

canvas.create_line(pontok,width=5,fill="purple")
pontok=eltol(pontok,0,100)
canvas.create_line(pontok,width=5,fill="purple")


fenyo1=[200,0,0,400,190,400,190,500,210,500,210,400,400,400,200,0]
pontok=eltol(fenyo1,10,10)
canvas.create_line(fenyo1,width=5,fill="green")
fenyo2=[200,0,0,100,150,100,0,200,150,200,0,300,150,300,150,400,250,400,250,300,400,300,250,200,400,200,250,100,400,100,200,0]

fenyo2=eltol(fenyo2,200,200)
canvas.create_line(fenyo2,width=5,fill="green")

win.mainloop()

