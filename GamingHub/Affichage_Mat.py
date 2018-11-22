
import numpy as np
from tkinter import *
root=Tk()
root.title("Working state")

frame = Frame(root)
frame.grid()
#Entry_theme
Entry_theme= Entry(root,width=50, text= "inserer le theme souhaité(1,2,3)")
Entry_theme.insert(0,"insérer le theme souhaité(1,2,3)")
Entry_theme.grid(row=0,column=4,sticky=W,padx=10)
Label(root, text="Théme:").grid(row=0,column=0,sticky=W,padx=10)

#Entry_size
Entry_size= Entry(root,width=50, text= "inserer la taille de la grille")
Entry_size.insert(0,'insérer la thaille de la grille')
Entry_size.grid(row=1,column=4,sticky=W,padx=10)
Label(root, text="Théme:").grid(row=0,column=0,sticky=W,padx=10)

Com=StringVar()
Com.set("ATTENTION REGARDEZ ICI EN JOUANT")
Commentaire= Entry(root, text= "ATTENTION REGARDEZ ICI EN JOUANT", textvariable=Com,width=50)
Commentaire.grid(row=2,column=4,sticky=W,padx=10)
Label(root, text="Taille:").grid(row=1,column=0,sticky=W,padx=10)

#----- Récupérer les entrées
def set_theme_grid():
    global Entry_theme
    theme=""
    i=0
    while not theme in ["0","1","2"]:

        theme = Entry_theme.get()
        if i>0:
            modif_commentaire("le théme doit être 0,1 ou 2")
        i+=1
    return theme

def set_size_grid():
    global Entry_size
    size=""
    i=0
    while not size.isdigit():

        size = Entry_size.get()
        if i>0:
           modif_commentaire( "Entrer un entier svp")

        i+=1
    return size

#--Cette partie dessine les boutons de jeu--

def modif_commentaire(text):
    global Commentaire
    Commentaire.delete(0,"end")
    Commentaire.insert(0,text)

command=StringVar()
def Afficher_bouton(dict):
    global Button_1, command
    for key, value in dict.items():

        Text1=StringVar()
        Button_1=Radiobutton(root,indicatoron=0,textvariable=Text1, variable=command,value=value[1])
        Button_1.grid(row=value[0][0], column=value[0][1], padx=2, sticky=E)
        Text1.set(key)


def waiting():
    global command
    Button_1.wait_variable(command)

def set_direction():
    global command
    waiting()
    print(command.get())

    return(command.get())

def Affiche_mat(A,root):

    #root= Tk() #à modifier si la fenêtre est deja créee

    nb_lignes=len(A)
    nb_colonnes=len(A[0])
    L=[]
    H=[]
    for i in range (0,nb_lignes):
        for j in range (0,nb_colonnes):
            #adresse_image=Dict[A[i][j]]
            #photo=PhotoImage(file=adresse_image)
            contenu=StringVar()
            contenu.set(A[i][j])
            L.append(contenu)
            label=Label(root,width=10,height=5,borderwidth=3,relief='groove',textvariable=contenu)#image=photo)
            label.grid(row=i+6,column=j+6)
            H.append(label)

    return(H,L)




