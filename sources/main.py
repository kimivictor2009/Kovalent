from tkinter import * 

'''
Note pour le stockage des atomes :
atomes = [{id : 3, nom : "C", pos : (x=127, y=208), liaisons : [(id=5, nb_liaisons=2), (etc)]}, {atome2}, {etc}]

type(atomes) = list[dict(int, str, tuple[int, int], list[tuple(int, int)])]

liste des atomes
atome = dictionnaire avec infos
infos : id, formule, position et liaisons

'''
# Molécule de CH2O
atomes = [{"id" : 1, "nom" : "C", "pos" : (127, 208), "liaisons" : [(2, 2), (3, 1), (4, 1)]},
          {"id" : 2, "nom" : "O", "pos" : (94, 215), "liaisons" : [(1, 2)]},
          {"id" : 3, "nom" : "H", "pos" : (131, 249), "liaisons" : [(1, 1)]},
          {"id" : 4, "nom" : "H", "pos" : (134, 157), "liaisons" : [(1, 1)]}]

HEIGHT = 40
WIDTH = 160

fenetre = Tk()

fenetre['bg']='white'

# frame principale
Frame = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame.pack(side=TOP, expand=Y, fill=BOTH, padx=0, pady=0)

Label(Frame, text="Frame principale", height=HEIGHT, width=WIDTH).pack(padx=0, pady=0)

fenetre.mainloop()