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
BetuSzinek=["Blue",hatter,"Blue","Blue","Blue",hatter]

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

print(R2,E2,K2,A2)

Reka=[[100, 100, 210, 100, 210, 190, 130, 190, 130, 220, 160, 220, 160, 250, 190, 250, 190, 280, 220, 280, 220, 250, 190, 250, 190, 220, 160, 220, 160, 190, 130, 190, 130, 290, 100, 290, 100, 100],
    [127.5, 122.5, 182.5, 122.5, 182.5, 167.5, 127.5, 167.5, 127.5, 122.5],
    [225.0, 114.0, 225.0, 264.0, 345.0, 264.0, 345.0, 234.0, 255.0, 234.0, 255.0, 204.0, 345.0, 204.0, 345.0, 174.0, 255.0, 174.0, 255.0, 144.0, 345.0, 144.0, 345.0, 114.0, 225.0, 114.0],
    [350, 110, 380, 110, 380, 185, 425, 110, 450, 110, 410, 185, 425, 260, 400, 260, 380, 185, 380, 260, 350, 260, 350, 110],
    [440.0, 260.0, 512.0, 260.0, 540.0, 200.0, 580.0, 200.0, 608.0, 260.0, 680.0, 260.0, 600.0, 100.0, 520.0, 100.0, 440.0, 260.0],
    [540.0, 180.0, 576.0, 180.0, 588.0, 120.0, 552.0, 120.0, 540.0, 180.0]]

while True:
    canvas.delete("all")
    Reka=transzformaciok.forgat(Reka,0.3)
    #canvas.create_polygon(R2,width=5,fill="white",outline="black")
    #canvas.create_polygon(E2,width=5,fill="white",outline="black")
    #canvas.create_polygon(K2,width=5,fill="white",outline="black")
    #canvas.create_polygon(A2,width=5,fill="white",outline="black")
    #R2=transzformaciok.forgat(R2,0.01)
    for i,e in enumerate(Reka):
        d=canvas.create_polygon(e,width=2,fill=BetuSzinek[i], outline="black")


    win.update_idletasks()
    win.update()

canvas.create_line(R[0],width=5,fill="pink")
canvas.create_line(R[1],width=5,fill="pink")
win.mainloop()