from Tkinter import *
from random import *

lista=list()
tot=0
#######################crear##########################
def crear():
    global tot
    tot=8
    cont=0
    global lista
    lista=[]
    for x in range(0,8):
        lista_aux=list()
        for y in range(0,8):
            x=randrange(0,9)
            if x == 0 or x==1:
                cont+=1
            if cont < 11:
                lista_aux.append(x)
            else:
                lista_aux.append(2)
        lista.append(lista_aux)
    for a in range(2,10):
        for b in range(2,10):
            Label(ventana,image=src).grid(column=a,row=b)
    Label(ventana,image=cara).grid(column=5,row=0,columnspan=2,rowspan=2)
    ventana.geometry("233x300+0+0")

def crear2():
    global tot
    tot=10
    cont=0
    global lista
    lista=[]
    for x in range(0,10):
        lista_aux=list()
        for y in range(0,10):
            x=randrange(0,9)
            if x == 0 or x==1:
                cont+=1
            if cont < 21:
                lista_aux.append(x)
            else:
                lista_aux.append(2)
        lista.append(lista_aux)
    for a in range(2,12):
        for b in range(2,12):
            Label(ventana,image=src).grid(column=a,row=b)
    Label(ventana,image=cara).grid(column=6,row=0,columnspan=2,rowspan=2)
    ventana.geometry("290x345+0+0")

#######################comandos#################
def perdiste():
    global tot
    for a in range(2,tot):
        for b in range(2,tot):
            if lista[a][b]<2:
                Label(ventana,image=bomba).grid(column=a,row=b)
            lista[a][b]=11


def abrir(x,y):
    bomb=0
    if lista[x-2][y-2]!=11:
        if lista[x-2][y-2]>1:
            for i in range(x-3,x):
                if i >=0 and i<tot:
                    for j in range(y-3,y):
                        if j>=0 and j<tot:
                            if lista[i][j]<=1:
                                bomb+=1
            if bomb==0:
                Label(ventana,image=blan).grid(column=x,row=y)
                lista[x-2][y-2]=11
                for a in range(x-1,x+2):
                     if a >=0 and a<tot:
                        for b in range(y-1,y+2):
                            if b>=0 and b<tot:
                                print abrir(a,b)
                                
            else:
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
            Label(ventana,image=asus).grid(column=5,row=0,columnspan=2)
            return perdiste()
        
def callback(event):
    grid_info=event.widget.grid_info()
    y=int(grid_info["row"])
    x=int(grid_info["column"])
    print x,y
    global tot
    if y >= 2:
        print abrir(x,y)
    else:
        print crear()
        for a in range(2,tot):
            for b in range(2,tot):
                Label(ventana,image=src).grid(column=a,row=b)
        Label(ventana,image=cara).grid(column=5,row=0,columnspan=2)
    
def band(event):
    grid_info=event.widget.grid_info()
    y=int(grid_info["row"])
    x=int(grid_info["column"])
    Label(ventana,image=bandera).grid(column=x,row=y)


ventana = Tk()
ventana.title("Busca Minas")
ventana.geometry("233x300+0+0")
###################imagenes#################################
src=PhotoImage(file="25.gif")
cara=PhotoImage(file="cara.gif")
bomba=PhotoImage(file="gear.gif")
asus=PhotoImage(file="cara2.gif")
bandera=PhotoImage(file="band.gif")
blan=PhotoImage(file="blanc.gif")
###################menu#####################################
menubar = Menu(ventana)
menu = Menu(menubar)
menu.add_command(label="8x8",command=crear)
menu.add_command(label="10x10",command=crear2)
menubar.add_cascade(label="Juego",menu=menu)
ventana.config(menu=menubar)
###################boton####################################
ventana.bind("<Button-1>", callback)
ventana.bind("<Button-3>", band)
ventana.mainloop()
