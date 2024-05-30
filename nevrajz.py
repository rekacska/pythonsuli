import transzformaciok 

from tkinter import *

#create an instance of tkinter frame or window 
win=Tk()

#Set the size of the tkinter window
win.geometry("600x600")

#Create a canvas widget 
canvas = Canvas(win, width=600, height=600)
canvas.configure(bg="white")
canvas.pack(fill=BOTH, expand=1) #teljes ablakot kitölti 

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


fenyo2Masolat = transzformaciok.eltol(fenyo2,100,100)
#canvas.create_line(fenyo2Masolat,width=5,fill="green")

R=[[    0,0,
        110,0,
        110,90,
        30,90,
        30,120,
        60,120,
        60,150,
        90,150,
        90,180,
        120,180,
        120,150,
        90,150,
        90,120,
        60,120,
        60,90,
        30,90,
        30,190,
        0,190,
        0,0
],[
        27.5,22.5,
        82.5,22.5,
        82.5,67.5,
        27.5,67.5,
        27.5,22.5,
]]

E=[0,0,
   0,500,
   400,500,
   400,400,
   100,400,
   100,300,
   400,300,
   400,200,
   100,200,
   100,100,
   400,100,
   400,0,
   0,0]

K=[0,0,
   30,0,
   30,75,
   75,0,
   100,0,
   60,75,
   75,150,
   50,150,
   30,75,
   30,150,
   0,150,
   0,0]

A=[[0,400,
   180,400,
   250,250,
   350,250,
   420,400,
   600,400,
   400,0,
   200,0,
   0,400],
   [250,200,
    340,200,
    370,50,
    280,50,
    250,200]]

hatter="#ffffff"
BetuSzinek=["Blue",hatter,hatter]

R2=transzformaciok.masol(R)
R2=transzformaciok.eltol(R2,100,100)
#R2=transzformaciok.forgat(R2,-45)

E2=transzformaciok.masol(E)
E2=transzformaciok.eltol(E2,750,380)
#E2=transzformaciok.forgat(E2,-45)
E2=transzformaciok.nagyit(E2,0.3)

K2=transzformaciok.masol(K)
K2=transzformaciok.eltol(K2,350,110)

A2=transzformaciok.masol(A)
A2=transzformaciok.eltol(A2,1100,250)
A2=transzformaciok.nagyit(A2,0.4)

#for e in R2:
 #   canvas.create_line(e,width=5,fill="pink",)

while True:
    canvas.delete("all")
    #canvas.create_polygon(R2,width=5,fill="white",outline="black")
    #canvas.create_polygon(E2,width=5,fill="white",outline="black")
    #canvas.create_polygon(K2,width=5,fill="white",outline="black")
    #canvas.create_polygon(A2,width=5,fill="white",outline="black")
    #R2=transzformaciok.forgat(R2,0.01)
    for i,e in enumerate(R2):
        d=canvas.create_polygon(e,width=2,fill=BetuSzinek[i], outline="black")
        l=canvas.create_polygon(E2,width=2,fill=BetuSzinek[i], outline="black")
        c=canvas.create_polygon(K2,width=2,fill=BetuSzinek[i], outline="black")
        p=canvas.create_polygon(A2,width=2,fill=BetuSzinek[i], outline="black")


    win.update_idletasks()
    win.update()

canvas.create_line(R[0],width=5,fill="pink")
canvas.create_line(R[1],width=5,fill="pink")
win.mainloop()