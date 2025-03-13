import tkinter as tk
from tkinter import simpledialog
from random import randint

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


#root = tk.Tk()

fenetre=tk.Tk()
fenetre.title("connerie")


canvas = tk.Canvas(fenetre, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background="black")
canvas.grid(row=1, column=1, rowspan=3)
couleur = "white"

def disque():
    x= randint(50, CANVAS_WIDTH-50)
    y= randint(50, CANVAS_HEIGHT-50)
    canvas.create_oval(x-50, y-50, x+50, y+50, fill=couleur)

def carre():
    x= randint(50, CANVAS_WIDTH-50)
    y= randint(50, CANVAS_HEIGHT-50)
    canvas.create_rectangle(x-50, y-50, x+50, y+50, fill=couleur)

def croix():
    x= randint(50, CANVAS_WIDTH-50)
    y= randint(50, CANVAS_HEIGHT-50)
    canvas.create_line(x-50, y, x+50, y, fill=couleur)
    canvas.create_line(x, y-50, x, y+50, fill=couleur)

def changer_couleur():
    global couleur
    couleur = simpledialog.askstring("Couleur", "Entrez une couleur:")

def fermer_fenetre():
    fenetre.destroy()
    

bouton = tk.Button(fenetre, text="Cercle", command=disque)    
bouton.grid(row=1, column=0)

bouton = tk.Button(fenetre, text="Carré", command=carre)
bouton.grid(row=2, column=0)

bouton = tk.Button(fenetre, text="Croix", command=croix)
bouton.grid(row=3, column=0)

bouton = tk.Button(fenetre, text="Couleur", command=changer_couleur)
bouton.grid(row=0, column=1)

bouton= tk.Button(fenetre, text="Fermer", command=fermer_fenetre)
bouton.grid(row=0, column=2)

fenetre.mainloop()