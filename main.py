from tkinter import *
from tkinter import messagebox

#Var globales para cuando inician las X
jugada = True
cont = 0

def ganador():
    global winner
    winner = False
    #CON X
    #Para cuando son las filas
    if a1["text"] == "X" and a2["text"] == "X" and a3["text"] == "X":
        winner = True
        messagebox.showinfo("Ganador", "Jugador X ha ganado")
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        winner = True
        messagebox.showinfo("Ganador", "Jugador X ha ganado")
    if c1["text"] == "X" and c2["text"] == "X" and c3["text"] == "X":
        winner = True
        messagebox.showinfo("Ganador", "Jugador X ha ganado")

    #Para cuando son las columnas
    if a1["text"] == "X" and b1["text"] == "X" and c1["text"] == "X":
        winner = True
        messagebox.showinfo("Ganador", "Jugador X ha ganado")
    if a2["text"] == "X" and b2["text"] == "X" and c2["text"] == "X":
        winner = True
        messagebox.showinfo("Ganador", "Jugador X ha ganado")
    if a3["text"] == "X" and b3["text"] == "X" and c3["text"] == "X":
        winner = True
        messagebox.showinfo("Ganador", "Jugador X ha ganado")

    #CON O
    # Para cuando son las filas
    if a1["text"] == "O" and a2["text"] == "O" and a3["text"] == "O":
        winner = True
        messagebox.showinfo("Ganador", "Jugador O ha ganado")
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        winner = True
        messagebox.showinfo("Ganador", "Jugador O ha ganado")
    if c1["text"] == "O" and c2["text"] == "O" and c3["text"] == "O":
        winner = True
        messagebox.showinfo("Ganador", "Jugador O ha ganado")

    # Para cuando son las columnas
    if a1["text"] == "O" and b1["text"] == "O" and c1["text"] == "O":
        winner = True
        messagebox.showinfo("Ganador", "Jugador O ha ganado")
    if a2["text"] == "O" and b2["text"] == "O" and c2["text"] == "O":
        winner = True
        messagebox.showinfo("Ganador", "Jugador O ha ganado")
    if a3["text"] == "O" and b3["text"] == "O" and c3["text"] == "O":
        winner = True
        messagebox.showinfo("Ganador", "Jugador O ha ganado")




#Funci??n para cuando se hace click
def click_tecla(tecla):
    global jugada, cont

    if tecla["text"] == "" and jugada == True: #Si la tecla/boton tiene su texto vac??o, y jugada es verdadero, entonces se realiza lo siguiente
        tecla["text"] = "X" #tambi??n se podr??a cambiar por O
        jugada = False #el turno de X termin??
        cont +=1
        ganador()
    elif tecla["text"] == "" and jugada == False: #Si la tecla/boton tiene su texto vac??o, y jugada es falso, entonces se realiza lo siguiente
        tecla["text"] = "O"
        jugada = True  # Pasa al turno de X
        cont += 1
    else:
        messagebox.showerror("Jugada no aceptada") #muestra mensaje de error porque se ha pulsado una tecla que ya est?? ocupada


#Se crea la ventana
from tkinter import messagebox

raiz = Tk()

# Se agrega t??tulo a la ventana
raiz.title("Totito")

# Se agregan los botones, se deja el texto vac??o, se les da un tama??o y altura, y se agrega el comando para agregar una acci??n o evento
a1 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(a1))
a2 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(a2))
a3 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(a3))

b1 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(b1))
b2 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(b2))
b3 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(b3))

c1 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(c1))
c2 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(c2))
c3 = Button(raiz, text="", height=3, width=6, command=lambda: click_tecla(c3))

# Se colocan los botones en el grid o malla, para que se vean como un tablero
a1.grid(row=0, column=0)
a2.grid(row=0, column=1)
a3.grid(row=0, column=2)

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

c1.grid(row=2, column=0)
c2.grid(row=2, column=1)
c3.grid(row=2, column=2)

raiz.mainloop()
