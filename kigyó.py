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

def rajzol():
     #labdaColor=atmenetColor(red,green,blue)
    labdaPos[0]+=labdaSpeed[0]*labdaSize
    labdaPos[1]+=labdaSpeed[1]*labdaSize

    if labdaPos[0]>win.winfo_width() or labdaPos[0]<0:
        labdaSpeed[0]*=-1
        #labdaColor=randomColor()

    if labdaPos[1]>win.winfo_width() or labdaPos[1]<0:
        labdaSpeed[1]*=-1
        #labdaColor=randomColor()



    labdaLista.append(canvas.create_oval(labdaPos[0],labdaPos[1],labdaPos[0]+labdaSize,labdaPos[1]+labdaSize,fill="lightblue"))
    kajaCheck()
    if len(labdaLista)>labdaListaHossz:
        #print(labdaLista[0])
        canvas.delete(labdaLista[0])
        labdaLista.pop(0)
        print(len(labdaLista),labdaListaHossz)
    win.after(jatekSpeed,rajzol)   


def gombLe(e):
    if e.keysym=="Up":
        print("Fel")
        labdaSpeed[0]=0
        labdaSpeed[1]=-1
    elif e.keysym=="Down":
        #print("Le")
        labdaSpeed[0]=0
        labdaSpeed[1]=1
    elif e.keysym=="Right":
        #print("Jobb")
        labdaSpeed[0]=1
        labdaSpeed[1]=0
    elif e.keysym=="Left":
        #print("Bal")
        labdaSpeed[0]=-1
        labdaSpeed[1]=0
    print(e)

kajak=[]
def kaja():
    x=random.randint(0,win.winfo_width()-kajaSize)
    y=random.randint(0,win.winfo_height()-kajaSize)
    kajak.append(canvas.create_oval(x,y,x+kajaSize,y+kajaSize,fill=labdaColor,outline=""))
    
    win.after(kajaSpeed,kaja)  
#def collisionDetection():
    #sb=playground.bbox(ship)
    #ab=playground.bbox(alien)
    #if ab[0]<sb[2]<ab[2]and ab[2]<sb[1]ab[3]:
           # playground.move(alien,50,50)

def kajaCheck():
    f=canvas.bbox(labdaLista[-1])
    fKozep=[(f[0]+f[2])/2,(f[1]+f[3])/2]

    for egyKaja in kajak:
        k=canvas.bbox(egyKaja)
        kKozep=[(k[0]+k[2])/2,(k[1]+k[3])/2]

        x=fKozep[0]-kKozep[0]
        y=fKozep[1]-kKozep[1]

        #eleri a kajat
        if x**2+y**2 <= (labdaSize+kajaSize)**2:
            print("hamm!")
        else:
            print("hetd")

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

labdaSpeed=[0,0]
kajaSpeed=5000
labdaPos=[200,100]
labdaSize=20
kajaSize=20
labdaColor="green"
red,green,blue=0,0,0
jatekSpeed=500
labdaLista=[]
labdaListaHossz=1

win.bind("<KeyPress>",gombLe)

win.after(jatekSpeed,rajzol)   
win.after(kajaSpeed,kaja)  
win.mainloop()