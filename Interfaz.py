from tkinter import *
from tkinter import messagebox

#Var globales para cuando inician las X
jugada = True
cont = 0

#Función para cuando se hace click
def click_tecla(tecla):
    global jugada, cont

    if tecla["text"] == "" and jugada == True: #Si la tecla/boton tiene su texto vacío, y jugada es verdadero, entonces se realiza lo siguiente
        tecla["text"] = "X" #también se podría cambiar por O
        jugada = False #el turno de X terminó
        cont +=1
    elif tecla["text"] == "" and jugada == False: #Si la tecla/boton tiene su texto vacío, y jugada es falso, entonces se realiza lo siguiente
        tecla["text"] = "O"
        jugada = True  # Pasa al turno de X
        cont += 1
    else:
        messagebox.showerror("Jugada no aceptada") #muestra mensaje de error porque se ha pulsado una tecla que ya está ocupada

def interfaz():
    #Se crea la ventana
    raiz = Tk()

    #Se agrega título a la ventana
    raiz.title("Totito")

    #Se agregan los botones, se deja el texto vacío, se les da un tamaño y altura, y se agrega el comando para agregar una acción o evento
    a1 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(a1))
    a2 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(a2))
    a3 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(a3))

    b1 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(b1))
    b2 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(b2))
    b3 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(b3))

    c1 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(c1))
    c2 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(c2))
    c3 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(c3))

    #Se colocan los botones en el grid o malla, para que se vean como un tablero
    a1.grid(row=0, column=0)
    a2.grid(row=0, column=1)
    a3.grid(row=0, column=2)

    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)

    c1.grid(row=2, column=0)
    c2.grid(row=2, column=1)
    c3.grid(row=2, column=2)

    winner = False
    if a1["text"] == "X" and a2["text"] == "X" and a3["text"] == "X":
        winner = True
        messagebox.showinfo("Ganador","Jugador X ha ganado")

    raiz.mainloop()