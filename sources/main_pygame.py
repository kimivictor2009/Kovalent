'''

==================== KOVALENT ====================


---------- NOTES ----------
    Note pour le stockage des atomes :
        atomes = [{id : 3, nom : "C", pos : (x=127, y=208), liaisons : [(id=5, nb_liaisons=2), (etc)]}, {atome2}, {etc}]

        type(atomes) = list[dict(int, str, tuple[int, int], list[tuple(int, int)])]

        liste des atomes
        atome = dictionnaire avec infos
        infos = id, formule, position et liaisons

---------- HISTORIQUE DES MODIFICATIONS ----------

=> VERSION 1
    -> Version 1.0, Victor
        - Création d'une fenêtre avec pygame
        - Frame dans la fenêtre de dimensions HEIGHT, WIDTH
    -> Version 1.1, Victor
        - Fonction render() pour tester
        - Affichage atomes et liaisons (TEST, sera supprimé)

==================== main.py ====================

'''

# -----<===== INITIALISATION =====>-----

# ----- Modules importés -----

from __future__ import annotations
import pygame as pg


# ----- Couleurs, constantes et initialisation de pygame -----

# Test pour une molécule de CH2O
atomes = [{"id" : 1, "nom" : "C", "pos" : (127, 208), "liaisons" : [(2, 2), (3, 1), (4, 1)]},
          {"id" : 2, "nom" : "O", "pos" : (94, 215), "liaisons" : [(1, 2)]},
          {"id" : 3, "nom" : "H", "pos" : (131, 249), "liaisons" : [(1, 1)]},
          {"id" : 4, "nom" : "H", "pos" : (134, 157), "liaisons" : [(1, 1)]}]


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


SCALE = 100 # Taille de la fenêtre en %, tout doit être proportionnel - peut être modifié à volonté

WINDOW_LENGHT = SCALE*6
WINDOW_HEIGHT = SCALE*6

WINDOW_SIZE = (WINDOW_LENGHT, WINDOW_HEIGHT)

pg.init()

surface = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("Kovalent")


def render() -> None :
    for atome in atomes :
        pg.draw.circle(surface, WHITE, (atome["pos"][0]*2, atome["pos"][1]*2), 10)
        for liaison in atome["liaisons"] :
            for atome2 in atomes :
                if atome2["id"] == liaison[0] :
                    pg.draw.line(surface, WHITE, (atome["pos"][0]*2, atome["pos"][1]*2), (atome2["pos"][0]*2, atome2["pos"][1]*2), 5*liaison[1])


running = True

while running == True :
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    surface.fill(BLACK)
    render()
    pg.display.flip()
    
pg.quit()

