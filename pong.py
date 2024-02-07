#Egyszerű pong játék
#Start: 2024.01.31
#Finish:
#Csicskó Réka
import random
from tkinter import *

def randomColor(): 
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    return ("#"+hex(red)[-2:]+hex(green)[-2:]+hex(blue)[-2:]).replace("x","0"),red,green,blue

def  atmenetColor(red, green, blue):
    red+=5
    if red>255:
        red=red-255
        green+5
    if green>255:
        green=green-255
        blue+5
    if blue>255:
        blue=blue-255
        red+5


jatekHatter="white"

print(randomColor())

win=Tk()
win.geometry("600x600+100+200")
win.title("pong játék 10.B/1, 2024")
canvas = Canvas(win, width=600, height=600, bg=jatekHatter)
#canvas.configure(bg="white")
canvas.pack(fill=BOTH, expand=1)

canvas.create_oval(0,0,100,100,fill="lightblue")

labdaSpeed=[1,1.5]
labdaPos=[200,100]
labdaSize=50
labdaColor="green"
red,green,blue=0,0,0
labdaListaHossz=5
labdaLista=[]
labdaLista

while True:
    labdaColor=atmenetColor(red,green,blue)
    labdaPos[0]+=labdaSpeed[0]
    labdaPos[1]+=labdaSpeed[1]

    if labdaPos[0]>win.winfo_width() or labdaPos[0]<0:
        labdaSpeed[0]*=-1
        #labdaColor=randomColor()

    if labdaPos[1]>win.winfo_width() or labdaPos[1]<0:
        labdaSpeed[1]*=-1
        #labdaColor=randomColor()



    labdaLista.append(canvas.create_oval(labdaPos[0],labdaPos[1],labdaPos[0]+labdaSize,labdaPos[1]+labdaSize,fill="lightblue"))
    if len(labdaLista)>labdaListaHossz:
        canvas.delte(labdaLista[0])
    canvas.update()

win.mainloop()