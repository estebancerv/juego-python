from Tkinter import *
from random import *

lista=list()
lista2=list()
src=0
bomba=0
bandera=0
blan=0
cara=0
asus=0

def ganaste():
    Label(ventana, text="Ganastes!!!",fg="deep pink"
          ,bg="black",font=("Helvetica 30 bold italic")).place(x=0,y=120)

def camb(event):
    global src
    global bomba
    global bandera
    global blan
    global cara
    global asus
    src=PhotoImage(file="como.gif")
    bomba=PhotoImage(file="tnt.gif")
    bandera=PhotoImage(file="bande.gif")
    blan=PhotoImage(file="tier.gif")
    cara=PhotoImage(file="car.gif")
    asus=PhotoImage(file="zom.gif")
    Label(ventana,text="Adri",fg="purple",font=("Helvetica 15 bold italic")).place(x=0,y=250)
    Label(ventana,text="Kikin",fg="blue",font=("Helvetica 15 bold italic")).place(x=170,y=250)

def crear():
    cont=0
    global lista
    lista=[]
    global lista2
    lista2=[]
    for x in range(0,8):
        lista_aux=list()
        lista2_aux=list()
        for y in range(0,8):
            lista2_aux.append(1)
            x=randrange(0,9)
            if x == 0 or x==1:
                cont+=1
            if cont < 11:
                lista_aux.append(x)
            else:
                lista_aux.append(2)
        lista2.append(lista2_aux)
        lista.append(lista_aux)
    print lista2
    print lista

def perdiste():
    for a in range(0,8):
        for b in range(0,8):
            if lista[a][b]<2:
                Label(ventana,image=bomba).grid(column=a,row=b)
    Label(ventana,text="Perdiste pe",fg="deep pink"
          ,bg="black",font=("Helvetica 30 bold italic")).place(x=0,y=120)
    Label(ventana,text="Piensa mas",fg="deep pink"
          ,bg="black",font=("Helvetica 15 bold italic")).place(x=0,y=170)


def abrir(x,y):
    global lista
    global lista2
    bomb=0
    if lista2[x][y]==1:
        if lista[x][y]>1:
            for i in range(x-1,x+2):
                if i >=0 and i<8:
                    for j in range(y-1,y+2):
                        if j>=0 and j<8:
                            if lista[i][j]<=1:
                                bomb+=1
            if bomb==0:
                Label(ventana,image=blan).grid(column=x,row=y)
                lista2[x][y]=0
                for a in range(x-1,x+2):
                     if a >=0 and a<8:
                        for b in range(y-1,y+2):
                            if b>=0 and b<8:
                                print abrir(a,b)
                                
            else:
                lista2[x][y]=0
                if bomb==1:
                    Label(ventana,text="1",fg="blue",bg="black",font=("Helvetica 13 bold italic")).grid(column=x,row=y)
                elif bomb==2:
                    Label(ventana,text="2",fg="red",bg="black",font=("Helvetica 13 bold italic")).grid(column=x,row=y)
                elif bomb==3:
                    Label(ventana,text="3",fg="yellow",bg="black",font=("Helvetica 13 bold italic")).grid(column=x,row=y)
                elif bomb==4:
                    Label(ventana,text="4",fg="green",bg="black",font=("Helvetica 13 bold italic")).grid(column=x,row=y)
                elif bomb==5:
                    Label(ventana,text="5",fg="white",bg="black",font=("Helvetica 13 bold italic")).grid(column=x,row=y)
                elif bomb==6:
                    Label(ventana,text="6",fg="DeepPink2",bg="black",font=("Helvetica 13 bold italic")).grid(column=x,row=y)
                elif bomb==7:
                    Label(ventana,text="7",fg="purple",bg="black",font=("Helvetica 13 bold italic")).grid(column=x,row=y)
                elif bomb==8:
                    Label(ventana,text="8",fg="salmon4",bg="black",font=("Helvetica 13 bold italic")).grid(column=x,row=y)

        else:
            Label(ventana,image=asus).grid(column=3,row=8,columnspan=2)
            return perdiste()
    ta=0
    for t in range(0,8):
         for a in range(0,8):
            if lista2[t][a]==1:
                 ta+=1
    if ta==0:
        return ganaste()
        
def callback(event):
    grid_info=event.widget.grid_info()
    y=int(grid_info["row"])
    x=int(grid_info["column"])
    print x,y
    if y < 8:
        print abrir(x,y)
    else:
        print crear()
        for a in range(0,8):
            for b in range(0,8):
                Label(ventana,image=src).grid(column=a,row=b)
        Label(ventana,image=cara).grid(column=3,row=8,columnspan=2)
    
def band(event):
    grid_info=event.widget.grid_info()
    y=int(grid_info["row"])
    x=int(grid_info["column"])
    if lista2[x][y]==1:
        Label(ventana,image=bandera).grid(column=x,row=y)
        lista2[x][y]=0
    else:
        Label(ventana,image=src).grid(column=x,row=y)
        lista2[x][y]=1


ventana = Tk()
ventana.title("BuscaMinas")
ventana.geometry("233x300+0+0")
global src
global bomba
global bandera
global blan
global cara
global asus
src=PhotoImage(file="25.gif")
cara=PhotoImage(file="cara.gif")
bomba=PhotoImage(file="gear.gif")
asus=PhotoImage(file="cara2.gif")
bandera=PhotoImage(file="band.gif")
blan=PhotoImage(file="blanc.gif")
Label(ventana,image=cara).grid(column=3,row=8,columnspan=2)
ventana.bind("<Button-1>", callback)
ventana.bind("<Button-2>", camb)
ventana.bind("<Button-3>", band)
ventana.mainloop()
