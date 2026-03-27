# -*- coding: utf-8 -*-

# Projet : Kovalent
# Auteurs : Victor Alaimo et Kimi Vandaele-Otozaki ("KVTeam")

'''
==================== KOVALENT ====================

Bandeau d'informations - tenir à jour !

Version : 10.1.3 VERSION FINALE

Dernière édition : Victor, 26/03/2026, 22h15


---------- COMMENTAIRE ----------

Après beaucoup de relectures, c'est enfin fini.

---------- NOTES ----------

    Note pour le stockage des atomes :
        atomes = [{id : 3, nom : "C", pos : (x=127, y=208), liaisons : [(id=5, nb_liaisons=2), (etc)]}, {atome2}, {etc}]

        type(atomes) = list[dict(int, str, tuple[int, int], list[tuple(int, int)])]

        liste des atomes
        atome = dictionnaire avec infos
        infos = id, formule, position et liaisons
    
    Penser à nommer les variables en anglais pour la réutilisation
    Penser aussi aux docstrings et aux commentaires
    Pas besoin de faire *SCALE pour du texte, la fonction le fait automatiquement
    Pas besoin de scale pour les boutons non plus
    et je le fais pas en une seule fois du coup ça fait plein de versions
    j'ai passé trop de temps sur la detect_win mais j'ai réussi UwU


---------- HISTORIQUE DES MODIFICATIONS ----------

=> VERSION 1
    -> Version 1.0, Victor
        - Création d'une fenêtre avec pygame
        - Frame dans la fenêtre de dimensions HEIGHT, WIDTH
    -> Version 1.1, Victor
        - Fonction render() pour tester
        - Affichage atomes et liaisons (TEST, sera supprimé)
    -> Version 1.2, Victor
        - Fonctions create_text() et print_text(), permettant d'afficher du texte dans la fenêtre
        - Structuration du code
    -> Version 1.3 Victor
        - Dimensionnage automatique de la fenêtre, qui s'adapte à l'écran principal
        - Variable fenetre_basique à changer pour avoir une fenêtre de dimension prédéfinie (pour les devs)
    -> Version 1.4 Victor
        - Ajout d'un ticker
        - Ajout d'une intro
        - Ajout d'un titre du menu
    -> Version 1.5 Victor
        - Police de caractère style futuriste
    -> Version 1.6 Victor
        - Fonction permettant de faire des boutons
        - Bouton "Jouer" (non fonctionnel, test)
        
=> VERSION 2
    -> Version 2.0 Victor
        - Problème avec la police, encore à régler
        - Problème avec screeninfo, encore à régler
        - Ajout d'une variable menu qui dit où on est
        - Ajout d'un bouton pour les régles du jeu
        - Effet des boutons (changer le menu)
        - Bouton de retour au menu principal
        - Petit effet stylé supplémentaire dans l'intro
        -> Version 2.0.1 : Changement des couleurs de boutons
        -> version 2.0.2 : Ajout d'une option pour mettre le font par défaut avec la variable default_font

=> VERSION 3
    -> Version 3.0 Victor
        - Ajout du menu de sélection des niveaux
        - Boutons de sélection des niveaux
        - Création de la fonction "game"
        - Menu de jeu basique
    -> Version 3.1 Kimi, Victor
        - Correction et relecture
        
=> VERSION 4
    -> Version 4.0 Kimi
        - création du Json
        - niveau et atomes importés
    -> Version 4.1 Victor
        - Règles de jeu très basiques rédigées et affichées
        - J'ai reglé le problème avec le bouton jouer
    -> Version 4.2 Victor
        - Début du module atomes avec un affichage des atomes
        - Convertissage du dict[list[dict]] atoms_data en list[dict] car plus simple et pratique
        - Fonction pour chercher un dictionnaire avec une clé avec une certaine valeur dans une liste
            pour chercher les infos sur l'atome à afficher
        - La couleur dans atoms_data est en string et pas en tuple[int, int, int] donc
            formatage des dict de la liste pour afficher les atomes dans la bonne couleur
    -> Version 4.3 Victor
        - Fixé le json
        - Ajout de liaisons
        - Début pour les liaisons doubles
        - Optimisation

=> VERSION 5
    -> Version 5.0 Victor
        - Liaisons doubles, triples, etc
        - Factorisation du code avec une nouvelle fonction
        - Visuel sur l'atome sélectionné avec un contour jaune

=> VERSION 6
    -> Version 6.0 Kimi
        - Déplacement des atomes
        - Modification de la fonction game
        - Création de la fonction"trouver_atome_avec_souris"

=> VERSION 7
    -> Version 7.0 Kimi
        - Niveau avec des infos sur chaque niveau (voir level_info)
        - Click droit pris en charge(voir click_droit)
        - Fonction permettant de creer des une liste de dictionnaire sur le modele choisis
          (voir create_id_for_each_atoms)(pour la molecule du niv 50 ça fait dans les 4000 caracteres :D)
    -> Version 7.1 Victor
        - Correction d'un bug avec les liaisons
    -> Version 7.2 Victor
        - Création des atomes selon le niveau
        - os.sep.join([]) pour compatibilité
        - Importation du module math
        - Disposition des atomes en cercle au départ
    -> Version 7.3 Victor
        - Limitation du déplacement des atomes à la zone de jeu
        - Disposition initiale des atomes en ovale corrigée
        - Tests pour régler un problème avec screeninfo
        - Try except pour la taille de la fenêtre
        - Aucun atome sélectionné au départ

=> VERSION 8
    -> Version 8.0 Victor
        - Renommage de certaines variables et fonctions en anglais (ça fait plus pro)
        - Fonction detect_win() qui indique si le joueur a gagné on non
        - Ajout de couleurs correspondant aux difficultés pour les boutons de sélection
        - Indication de la difficulté dans le menu de jeu
        - Ajout d'un arrière-plan pour les menus
    -> Version 8.1 Victor
        - Niveau 50 désormais "impossible", en noir
        - Modif du font

=> VERSION 9
    -> Version 9.0 Kimi
        -creation des liaison limitée selon la valence et le nombre de liaisons presente(voir create link)
        -ajout du background dans le jeu
        -ajout d'un bouton niveau suivant qui se debloque seulement quand on gagne
        -modification brève de la fonction background pour qu'elle soit utilisable avec des couleurs differentes
    -> Version 9.1 Victor
        - Ajout d'une icône de la fenêtre (quali de ouf)
        - Bouton pour quitter proprement
        - Ajustements divers
        - Changement du titre
    -> Version 9.2 Kimi
        -Réglage d'un bug qui faisait que les couleurs ne changeait pas entre les difficultés
        -Ajout d'un easter egg à ne jamais utiliser(PG5)(niveau 51 qui sait?) mais qui peut être un fun fact pédagogique
    -> Version 9.3 Victor
        - Bouton permettant de désactiver l'arrière-plan
        - Bouton permettant de recommencer le jeu (sans image pour l'instant)
    -> Version 9.4 Victor
        - Bouton restart avec image
    -> Version 9.5 Victor
        - Menu des règles modifié, avec changement du texte et plus de pages
        - Petite modification de l'intro
        -> Version 9.5.1 : J'ai tout cassé mais t'inquiète pas je gère
    -> Version 9.6 Victor
        - Début détection de victoire
        - Règles
        - Correction d'un bug avec niveau suivant
    -> Version 9.7 Victor
        - Enfin une vraie piste pour la détection de victoire
        - Niveau bloqués avec le cadenas

=> VERSION 10
    -> Version 10.0 Victor
        - Finalisation de la détection de la victoire en partie grâce au prof
        - Blocage des niveaux fonctionnel
        - Menu des crédits (dans informations)
        - Bouton easter egg ;)
    -> Version 10.1 Victor (version finale ?)
        - Correction d'un bug avec le bouton de niveau suivant
        - Optimisation du jeu (appel moins fréquent de la détection de la victoire)
        - Ajustement du Json par Kimi
        -> Version 10.1.1 : bug avec les liaisons corrigé
        -> Version 10.1.2 : en-tête et changement import fichiers et bug de dernière minute
        -> Version 10.1.3 : optimisation finale et relecture
        

==================== main.py ====================
'''


# -----<===== INITIALISATION =====>-----

# ----- Modules importés -----

from __future__ import annotations
import pygame as pg
import json
from math import *
import os
from screeninfo import *

# ----- Fichiers json importés -----

#kimi

with open(os.sep.join(['..', 'data', 'niveau.json']), 'r',encoding="utf-8") as file:
    levels_data = json.load(file) # importe le dict json sous le nom de levels_data
with open(os.sep.join(['..', 'data', 'atome.json']), 'r',encoding="utf-8") as fichier:
    atoms_data = json.load(fichier) # importe le dict json sous le nom de atoms_data

atoms_data = atoms_data["atome"] # maintenant c'est plus un dict c'est une list
levels_data = levels_data["niveau"]

#Easter egg à ne surtout pas mettre en marche
#PG5={ "nom": "PG5", "formule_brute":"C466591H444741N22147O22147", "atomes":["C"]*466591 + ["H"]*444741 + ["N"]*22147 + ["O"]*22147}
#print(PG5["atomes"][600000])
#levels_data.append(PG5)
#print(levels_data[51])


# Formatage des couleurs
# Victor

for i in range(len(atoms_data)) :
    atoms_data[i]["couleur"] = tuple(atoms_data[i]["couleur"])


# ----- Couleurs, constantes et variables/tableaux/autres -----

current_level = 0
fenetre_basique = False
skip_intro = False

if skip_intro :
    tick = 200
else :
    tick = 0

# Test pour une molécule de CH2O (chaque ligne est un atome)
atoms = [{"id" : 1, "name" : "C", "pos" : (702, 493), "links" : [(2, 2), (3, 1), (4, 1)]},
          {"id" : 2, "name" : "O", "pos" : (376, 430), "links" : [(1, 2)]},
          {"id" : 3, "name" : "H", "pos" : (868, 631), "links" : [(1, 1)]},
          {"id" : 4, "name" : "H", "pos" : (684, 314), "links" : [(1, 1)]}]


BLACK = (0, 0, 0)
DARK_GREY = (100, 100, 100)
LIGHT_GREY = (200, 200, 200)
WHITE = (255, 255, 255)
YELLOW = (230, 230, 0)
GREEN = (0, 200, 0)
ORANGE = (200, 100, 0)
RED = (200, 0, 0)
PURPLE = (100, 0, 150)
GRAY = (120, 120, 120)

def merge_colors(col1 : tuple, col2 : tuple) -> tuple :
    '''Produit une couleur moyenne des deux couleurs entrées'''
    col3 = ((col1[0]+col2[0])/2, (col1[1]+col2[1])/2, (col1[2]+col2[2])/2)
    return col3

print("\n") # Petit espace dans le shell pour les message d'erreur

mouse_pressed = False
mouse_pressed_right = False
moving = False
moved_atom_id = None
selected_atom = 0
difficulty = ""
level_color = ()
bg_on = True
page = 1
has_won = False
vict_start_tick = 0
locked = 3 # niveau bloqués sont les 3 et plus
give_money = False
gm_tick = 0
win = False

# ----- Initialisation de pygame et création de la fenêtre -----

# Par Victor

WINDOW_HEIGHT = 700
WINDOW_LENGHT = 1050

PROP_WINDOW = 1.5  # la proportion de la longueur sur la hauteur

if not fenetre_basique :
    # Parcoure les moniteurs et prend le principal
    try :
        for m in get_monitors() :
            if m.is_primary : # Le moniteur principal
        
                if (m.height - 150)*PROP_WINDOW <= m.width : # Si la fenêtre est assez large par rapport à ce qu'on veut si on prend la hauteur en modèle
            
                    WINDOW_HEIGHT = m.height - 150 # le 150 est une distance entre le bord haut et bas et la fenêtre
                    WINDOW_LENGHT = WINDOW_HEIGHT * PROP_WINDOW
            
                else :  # Sinon
             
                    WINDOW_LENGHT = m.width - 50
                    WINDOW_HEIGHT = WINDOW_LENGHT / PROP_WINDOW
    except :
        print("Erreur ! Le module screeninfo n'a pas fonctionné comme prévu ! Veuillez vérifier la version (0.8.1) et relancez le programme si besoin.")
        print("------------------------------")
        print("Initialisation du jeu avec une fenêtre de taille prédéfinie...")
        print("------------------------------")
    
        WINDOW_HEIGHT = 700
        WINDOW_LENGHT = 1050
    


SCALE = WINDOW_HEIGHT/800
# Correspond à la taille de la fenêtre, tout doit être proportionnel
# SCALE vaut 1.0 si la fenêtre à une hauteur (par défaut) de 800px, ce qui correspond à celle de fenetre_basique
# ATTENTION C'EST UN FLOAT
# Pas besoin de faire *SCALE pour du texte, la fonction le fait automatiquement



WINDOW_SIZE = (WINDOW_LENGHT, WINDOW_HEIGHT)

pg.init()

surface = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("Kovalent")

title = pg.transform.scale(pg.image.load(os.sep.join(['..', "data", "title.png"])), (800*SCALE, 100*SCALE))
restart_btn = pg.transform.scale(pg.image.load(os.sep.join(['..', "data", "restart.png"])), (50*SCALE, 50*SCALE))
lock_img = pg.transform.scale(pg.image.load(os.sep.join(['..', "data", "lock.png"])), (40*SCALE, 45*SCALE))

icon = pg.transform.scale(pg.image.load(os.sep.join(['..', "data", "icon.png"])), (32, 32))
pg.display.set_icon(icon)

# ----- Fonts -----

# Par Victor

prop_txt = 1.5 # change la taille de tous les textes (si on change de police, permet de switcher rapidement)

pg.font.init()

fichier_font = "freesansbold.ttf"

try :
    ftest = pg.font.SysFont(fichier_font, 20) # Si l'import du fichier ne marche pas, on prend celui par défaut
except :
    fichier_font = pg.font.get_default_font()
    print("Échec de l'import de la police de caractère")
    print("Démarrage avec la police par défaut...")


def create_text(text : str, size : int, color : tuple = WHITE) -> pg.Surface : # Par Victor
    '''Renvoie une Surface de texte, à blit pour afficher'''
    
    font = pg.font.SysFont(fichier_font, int(size*prop_txt)) # Un peu "laggy" des fois mais c'est pas grave
        
    return font.render(text, True, color)


def print_txt(text : str, pos : tuple, size : int = 30, color : tuple = WHITE, center : bool=False, dest = surface) -> None : # Par Victor
    '''Affiche du texte dans la fenêtre, mis automatiquement à son échelle'''
    
    s = create_text(text, int(size*SCALE), color)
    if center :
        dest.blit(s, (int(pos[0]*SCALE)-s.get_width()/2, int(pos[1]*SCALE)-s.get_height()/2.5))
    else :
        dest.blit(s, (int(pos[0]*SCALE), int(pos[1]*SCALE)))


# -----<===== FONCTIONS PRINCIPALES =====>-----

def click() -> bool:# Kimi
    global mouse_pressed
    
    if pg.mouse.get_pressed()[0]:
        if not mouse_pressed:
            mouse_pressed = True
            return True
    else:
        mouse_pressed = False
    
    return False

def right_click() -> bool:#Kimi
    global mouse_pressed_right
    
    if pg.mouse.get_pressed()[2]:
        if not mouse_pressed_right:
            mouse_pressed_right = True
            return True
    else:
        mouse_pressed_right = False
    
    return False


def render() -> None : # Par Victor
    '''Affiche tout ce qu'il faut afficher à l'écran'''
    
    global menu
    
    # Les 200 premiers ticks sont pour une petite intro
    
    if tick < 200 :
        menu = "main"
        intro()
    else :
        if menu == "main" :
            main_menu()
        elif menu == "level select" :
            level_select()
        elif menu == "rules" :
            rules()
        elif menu == "game":
            game()


def intro() -> None : # Par Victor
    '''Fait une intro des ticks 0 à 200'''
    if tick < 20 :
        surface.fill(BLACK)
    elif tick <= 80 :
        surface.fill(BLACK)
        teinte = ((tick-20)/60)*255
        print_txt("KVTeam", (600, 350), 50, (teinte, teinte, teinte), True)
        pg.draw.rect(surface, BLACK, ((200 + 200-((tick-20)/60)*200)*SCALE, 200*SCALE, 200*SCALE, 600*SCALE))
        pg.draw.rect(surface, BLACK, ((800 - 200+((tick-20)/60)*200)*SCALE, 200*SCALE, 200*SCALE, 600*SCALE))
    elif tick >= 170 :
        surface.fill(BLACK)
        teinte = (1-((tick-170)/30))*255
        print_txt("KVTeam", (600, 350), 50, (teinte, teinte, teinte), True)


def main_menu() -> None : # Par Victor
    '''Affiche le menu principal'''
    global menu, running, bg_on, page
    
    surface.fill(DARK_GREY)
    background(GRAY)
    
    surface.blit(title, (200*SCALE, 100*SCALE))
    
    if button((450, 300, 300, 100), "Jouer", BLACK, 50, LIGHT_GREY, WHITE) :
        menu = "level select"
    
    if button((400, 500, 400, 100), "Informations", BLACK, 50, LIGHT_GREY, WHITE) :
        menu = "rules"
        page = 1
    
    if button((970, 720, 200, 50), "Quitter", BLACK, 35, (255, 0, 0), merge_colors(WHITE, (255, 0, 0))) :
        running = False
    
    print_txt("Arrière-plan :", (10, 750), 40, BLACK, False)
    if bg_on :
        if button((285, 745, 180, 50), "Activé", BLACK, 35, GREEN, merge_colors(GREEN, WHITE)) :
            bg_on = False
    else :
        if button((275, 745, 200, 50), "Désactivé", BLACK, 35, LIGHT_GREY, merge_colors(LIGHT_GREY, WHITE)) :
            bg_on = True


def rules() -> None : # Par Victor
    '''Affiche le menu des règles du jeu'''
    global menu, page, give_money, gm_tick

    surface.fill(DARK_GREY)
    background(GRAY)
    
    print_txt("Page " + str(page) + "/4", (600, 700), 40, WHITE, True)
    
    if page == 1 :
        print_txt("Informations sur le projet", (600, 100), 80, WHITE, True)
        print_txt("Règles du jeu", (600, 200), 50, WHITE, True)
        
        print_txt("Le but du jeu est de relier les atomes entre eux en", (150, 300), 30, WHITE, False)
        print_txt("respectant leur nombre de valence (voir page 3). Vous devez former", (150, 350), 30, WHITE, False)
        print_txt("une molécule avec ces atomes, avec une structure libre.", (150, 400), 30, WHITE, False)
        print_txt("Il y a 50 niveaux, de plus en plus difficiles, à résoudre,", (150, 450), 30, WHITE, False)
        print_txt("les difficultés allant de facile à impossible. Pour débloquer un", (150, 500), 30, WHITE, False)
        print_txt("niveau et ainsi progresser, il faut d'abord finir le précédent.", (150, 550), 30, WHITE, False)
        
        if button((850, 650, 300, 100), "Suivant", BLACK, 60, LIGHT_GREY, WHITE) :
            page = 2
        if button((50, 650, 300, 100), "Menu", BLACK, 60, LIGHT_GREY, WHITE) :
            menu = "main"
            give_money = False
    
    elif page == 2 :
        print_txt("Informations sur le projet", (600, 100), 80, WHITE, True)
        print_txt("Instructions", (600, 200), 50, WHITE, True)
        
        print_txt("Vous pouvez bouger les différents atomes au sein de l'aire de", (150, 300), 30, WHITE, False)
        print_txt("jeu en les faisant glisser à l'aide de la souris.", (150, 350), 30, WHITE, False)
        print_txt("Cliquez sur un atome pour le sélectionner, et faites un", (150, 400), 30, WHITE, False)
        print_txt("clic droit sur un autre atome pour créer un lien entre les deux.", (150, 450), 30, WHITE, False)
        print_txt("En cliquant plusieurs fois sur l'atome de destination, changez", (150, 500), 30, WHITE, False)
        print_txt("la force du lien (double, triple...) ou supprimez-le.", (150, 550), 30, WHITE, False)
        
        if button((850, 650, 300, 100), "Suivant", BLACK, 60, LIGHT_GREY, WHITE) :
            page += 1
        if button((50, 650, 300, 100), "Précédent", BLACK, 50, LIGHT_GREY, WHITE) :
            page -= 1
    
    elif page == 3 :
        print_txt("Informations sur le projet", (600, 100), 80, WHITE, True)
        print_txt("Atomes", (600, 200), 50, WHITE, True)
        
        print_txt("Au cours du jeu, vous croiserez plusieurs atomes différents.", (150, 300), 30, WHITE, False)
        print_txt("Chacun a un nombre de liaisons avec d'autres atomes à respecter.", (150, 350), 30, WHITE, False)
        print_txt("Par exemple, l'atome de carbone (C) peut avoir 4 liaisons au total,", (150, 400), 30, WHITE, False)
        print_txt("ou alors 2 liaisons doubles, ou encore 1 triple et 1 simple. L'atome", (150, 450), 30, WHITE, False)
        print_txt("d'hydrogène (H), lui, ne peut en avoir qu'une seule.", (150, 500), 30, WHITE, False)
        
        if button((850, 650, 300, 100), "Suivant", BLACK, 60, LIGHT_GREY, WHITE) :
            page += 1
        if button((50, 650, 300, 100), "Précédent", BLACK, 50, LIGHT_GREY, WHITE) :
            page -= 1
    
    elif page == 4 :
        print_txt("Informations sur le projet", (600, 100), 80, WHITE, True)
        print_txt("Crédits", (600, 200), 50, WHITE, True)
        
        print_txt("Merci à notre duo de développeurs acharnés :", (150, 250), 30, WHITE, False)
        print_txt('''Victor et Kimi (ou "KVTeam" comme on aime s'appeler)''', (150, 290), 30, WHITE, False)
        print_txt("Projet réalisé en python, avec Pygame", (150, 330), 30, WHITE, False)
        print_txt("Police de caractère : free sans bold (inclue dans pygame)", (150, 370), 30, WHITE, False)
        print_txt("Tous les assets du jeu ont été réalisés par Victor.", (150, 410), 30, WHITE, False)
        print_txt("Remerciments à Fabien Rymland-Ergueta (professeur)", (150, 450), 30, WHITE, False)
        print_txt("pour les conseils techniques", (150, 490), 30, WHITE, False)
        print_txt("Et merci à VOUS, qui jouez à notre jeu :)", (150, 540), 35, WHITE, False)
        
        if button((50, 650, 300, 100), "Précédent", BLACK, 50, LIGHT_GREY, WHITE) :
            page -= 1
        
        if button((850, 650, 300, 100), "Compris !", BLACK, 55, LIGHT_GREY, WHITE) :
            menu = "main"
            give_money = False
        
        if not give_money :
            if button((950, 600, 200, 40), "Donner des sous", BLACK, 20, YELLOW, merge_colors(YELLOW, WHITE)) :
                give_money = True
                gm_tick = tick
        else :
            print_txt("Merci mais on n'est pas des voleurs", (950, 610), 20, YELLOW, True)
            print_txt("(Mais on peut vous débarrasser de votre argent si vous voulez vraiment)", (920, 630), 15, YELLOW, True)
            if tick - gm_tick > 230 :
                give_money = False
        
            


def level_select() : # Victor
    '''Affiche le menu de sélection du niveau à jouer'''
    global menu, current_level, difficulty, level_color, selected_atom, atoms, has_won, win
    
    surface.fill(DARK_GREY)
    background(GRAY)
    
    print_txt("Sélectionnez un niveau", (600, 80), 70, WHITE, True)

    if button((50, 650, 300, 100), "Retour", BLACK, 60, LIGHT_GREY, WHITE):
        menu = "main"


    num = 1
    for l in range(5):
        for i in range(10):
            x_pos = 150 + i * 100 - 30
            y_pos = 200 + l * 90 - 30
            
            if l == 0 :
                col = GREEN
            elif l == 1 :
                col = YELLOW
            elif l == 2 :
                col = ORANGE
            elif l == 3 :
                col = RED
            elif l == 4 and i < 9 :
                col = PURPLE
            else :
                col = (0, 0, 150)

            if num < locked :
                b = button((x_pos, y_pos, 60, 60), str(num), BLACK, 30, merge_colors(col, LIGHT_GREY), merge_colors(merge_colors(col, LIGHT_GREY), WHITE))
            else :
                button((x_pos, y_pos, 60, 60), "", BLACK, 30, merge_colors(col, BLACK), merge_colors(col, BLACK))
                surface.blit(lock_img, ((x_pos+10)*SCALE, (y_pos+7.5)*SCALE))
                b = False
            
            if b :
                current_level = num # On enregistre le niveau
                level_info = levels_data[num-1]
                atoms = create_atoms(current_level)
                menu = "game"
                has_won = False
                win = False
                selected_atom = 0
                                
                if current_level <= 10 :
                    difficulty = "Facile"
                    level_color = GREEN
                elif current_level <= 20 :
                    difficulty = "Normal"
                    level_color = YELLOW
                elif current_level <= 30 :
                    difficulty = "Difficile"
                    level_color = ORANGE
                elif current_level <= 40 :
                    difficulty = "Expert"
                    level_color = RED
                elif current_level <= 49 :
                    difficulty = "Maître"
                    level_color = PURPLE
                else :
                    difficulty = "Impossible"
                    level_color = BLACK
                
            num += 1


def game(): # Kimi et Victor
    '''Affiche le jeu'''
    global menu, selected_atom, moving, moved_atom_id, current_level, atoms, has_won, vict_start_tick, locked, win
    
    surface.fill(DARK_GREY)
    background(merge_colors(level_color, DARK_GREY)) # kimi
    level_info(current_level)
    
    if win :
        if not has_won :
            vict_start_tick = tick
            if current_level == locked-1 :
                locked += 1
        has_won = True
    
    if button((15, 15, 190, 30), "Menu", BLACK, 20, LIGHT_GREY, WHITE):
        menu = "level select"
        moving = False # Sécu
        has_won = False
        win = False
    
    if current_level < locked-1 and current_level<50:#kimi
        if button((15, 45, 190, 30), "Niveau suivant", BLACK, 20, LIGHT_GREY, WHITE) :
            current_level += 1
            atoms = create_atoms(current_level)
            selected_atom = 0
            moving = False
            moved_atom_id = None
            has_won = False
            win = False
            
    elif has_won and current_level==50:
        if button((15, 45, 190, 30), "Fin ?", BLACK, 20, LIGHT_GREY, WHITE) :
            current_level += 1
            atoms = create_atoms(current_level)
            selected_atom = 0
            moving = False
            moved_atom_id = None
            has_won = False
            win = False
            
    elif current_level == locked-1 and current_level < 50: #kimi
        if button((15, 45, 190, 30), "Niveau suivant", BLACK, 20, DARK_GREY, DARK_GREY) :
            moving = False
    
    
    if button((215, 15, 60, 60), "", BLACK, 20, LIGHT_GREY, WHITE):
        atoms = create_atoms(current_level)
        selected_atom = 0
        has_won = False
        win = False
    surface.blit(restart_btn, (220*SCALE, 20*SCALE))
    
    
    mx, my = pg.mouse.get_pos()
    is_clicking = pg.mouse.get_pressed()[0]
    #is_right_clicking = pg.mouse.get_pressed()[2] sert a rien pour l'instant

    if click(): # Si on clique
        move_target = find_atom_under_mouse(atoms)
        if move_target != None :
            selected_atom = move_target 
            moved_atom_id = move_target
            moving = True
            #print(selected_atom)
        else :
            selected_atom = 0
            #print(selected_atom)
    
    create_links()   
            
    # relâche le bouton
    if not is_clicking:
        moving = False
        moved_atom_id = None

    # Mise à jour de la position
    if moving and moved_atom_id != None :
        for atome in atoms:
            if atome["id"] == moved_atom_id and my > 150*SCALE and my < 740*SCALE and mx > 60*SCALE and mx < 1140*SCALE :
                # IMPORTANT  on divise par SCALE == SUPER CHIANT MERCI VICTOR
                # mais non je rigole t'étais obligé
                # en fait jsp si t'étais obligé mais ça marche et c'est bien
                atome["pos"] = (mx / SCALE, my / SCALE)

    display_atoms(atoms)
    
    
    if has_won :
        #print(sqrt(sin((tick - vict_start_tick)/80*pi))*80)
        if tick - vict_start_tick < 40 :
            print_txt("Niveau résolu !", (600, 400), sqrt(sin((tick - vict_start_tick)/80*pi))*80, WHITE, True)
        else :
            print_txt("Niveau résolu !", (600, 400), 80, WHITE, True)
            
    
    #print(mouse_pressed)
    #print_txt("Debug : mousepos=" + str(pg.mouse.get_pos()) + ", win=" + str(detect_win()), (600, 750), 30, WHITE, True)



def create_links() -> None:#kimi
    """gère les liaison entre atomes"""
    global selected_atom, win
    
    target_id = find_atom_under_mouse(atoms)
    
    if right_click() and target_id != None and selected_atom != 0 and target_id != selected_atom:
        
        atom1 = find_in_dlist(atoms, "id", selected_atom)
        atom2 = find_in_dlist(atoms, "id", target_id)
        atom1_valence = find_valence(atom1['name'])
        atom2_valence = find_valence(atom2['name'])
        #print(atom1["links"][0][1])
        if atom1_valence < atom2_valence and atom1_valence < 3 :
            atom12_valence = atom1_valence
        elif atom2_valence <= atom1_valence and atom2_valence <= 3 :
            atom12_valence = atom2_valence
        else:
            atom12_valence = 3
        
        
        liaison_existante_1 = None
        for l in atom1["links"]:
            if l[0] == target_id:
                liaison_existante_1 = l
                break
                
        liaison_existante_2 = None
        for l in atom2["links"]:
            if l[0] == selected_atom:
                liaison_existante_2 = l
                break
        
        atom1_nb_liaisons = 0
        for i in atom1["links"]:
            atom1_nb_liaisons += int(i[1])
        #print(atom1_nb_liaisons)
        
        atom2_nb_liaisons = 0
        for i in atom2["links"]:
            atom2_nb_liaisons += int(i[1])
        #print(atom2_nb_liaisons)

        if liaison_existante_1 == None :
            if atom1_nb_liaisons<atom1_valence and atom2_nb_liaisons<atom2_valence:
                atom1["links"].append((target_id, 1))
                atom2["links"].append((selected_atom, 1))
            
        else:
             
            atom1["links"].remove(liaison_existante_1)
            atom2["links"].remove(liaison_existante_2)
            nb_liaisons = liaison_existante_1[1]
            
            if nb_liaisons < atom12_valence and atom1_nb_liaisons<atom1_valence and atom2_nb_liaisons<atom2_valence: 
                atom1["links"].append((target_id, nb_liaisons + 1))
                atom2["links"].append((selected_atom, nb_liaisons + 1))
            
        win = detect_win()
        
        
        


def find_valence(atom_name:str)->int:#kimi optimisé par Victor avec appel de la fonction find_in_dlist
    """trouve le nombre de valence d'un atome"""
    
    return find_in_dlist(atoms_data, "symbole", atom_name)["valence"]


def scaling(pos : tuple) -> tuple[int, int] : # Par Victor
    '''Prend une paire de coordonnées et la renvoie après l'avoir mise à l'échelle'''
    x = int(pos[0]*SCALE)
    y = int(pos[1]*SCALE)
    return (x, y)


def lines_moved(spacing, s, p, p2) -> None : # désolé mais j'ai la flemme de spécifier une fonction qui ne sert qu'une fois - Par Victor
    '''Utile uniquement pour la fonction display_atoms(), pour gagner de la place, vu la répétition'''
    size = int(s*SCALE)
    
    # Kalkuls matématik (pas du tout copiés du professeur, voyons...)
    
    vect_x = p[0]-p2[0]
    vect_y = p[1]-p2[1]
    
    truc = (spacing*sqrt(vect_x**2+vect_y**2)) # jsp comment nommer la variable j'ai plus d'inspi
    # spacing est en unité cheloue, mais en gros plus c'est petit, plus les lignes s'écartent du centre
     
    x = p[0]+(vect_y/truc)
    y = p[1]-(vect_x/truc)
    x2 = p2[0]+(vect_y/truc)
    y2 = p2[1]-(vect_x/truc)
    pg.draw.line(surface, LIGHT_GREY, scaling((x, y)), scaling((x2, y2)), size)
    
    x = p[0]-(vect_y/truc)
    y = p[1]+(vect_x/truc)
    x2 = p2[0]-(vect_y/truc)
    y2 = p2[1]+(vect_x/truc)
    pg.draw.line(surface, LIGHT_GREY, scaling((x, y)), scaling((x2, y2)), size)


def find_atom_under_mouse(liste_atomes: list) -> int | None : # Kimi
    '''Renvoie l'ID de l'atome ou None si vide'''
    mx, my = pg.mouse.get_pos()
    for atome in liste_atomes:
        # On récupère les infos de l'atome (rayon) dans le JSON
        info = find_in_dlist(atoms_data, "symbole", atome["name"])
        rayon_ecran = info["rayon"] * SCALE
        # Position 
        ax, ay = scaling(atome["pos"])
        # Calcul de la distance
        distance = sqrt((mx - ax)**2 + (my - ay)**2)
        
        if distance <= rayon_ecran:
            return atome["id"]
    return None



def display_atoms(a : list) -> None : # Par Victor
    '''Affiche les atomes de la liste entrée et leur liaisons'''
    
    for i in range(len(a)) : # pour chaque atome
        p = a[i]["pos"]
        for j in a[i]["links"] :
            if a.index(find_in_dlist(atoms, "id", j[0])) > i :
                p2 = find_in_dlist(atoms, "id", j[0])["pos"]
                
                if j[1] == 1 : # Liaison simple
                    pg.draw.line(surface, LIGHT_GREY, scaling(p), scaling(p2), int(10*SCALE))
                    
                elif j[1] == 2 : # Liaison double
                    size = 8.5
                    spacing = 0.1
                    
                    lines_moved(spacing, size, p, p2)
                    
                elif j[1] == 3 : # Liaison triple
                    size = 7
                    spacing = 0.07
                    
                    lines_moved(spacing, size, p, p2)
                    
                    pg.draw.line(surface, LIGHT_GREY, scaling(p), scaling(p2), size)
                    
                elif j[1] == 4 : # Liaison quadruple
                    size = 6
                    
                    spacing = 0.05
                    lines_moved(spacing, size, p, p2)
                    
                    spacing = 0.15
                    lines_moved(spacing, size, p, p2)
            
            
    for i in a : # pour chaque atome
        a_info = find_in_dlist(atoms_data, "symbole", i["name"])
        p = i["pos"]
        pg.draw.circle(surface, a_info["couleur"], scaling(p), a_info["rayon"]*SCALE)
        if i["name"] == "C" :
            print_txt(i["name"], p, a_info["rayon"]*1.3, WHITE, True) # Juste pour le carbone, on met le symbole en blanc (vu qu'il est noir)
        else :
            print_txt(i["name"], p, a_info["rayon"]*1.3, BLACK, True)
        if i["id"] == selected_atom :
            pg.draw.circle(surface, YELLOW, scaling(p), (a_info["rayon"]+10)*SCALE, 5)




def find_in_dlist(t : list[dict], key : str, value : object) -> dict : # Par Victor
    '''Recherche dans t le premier dictionnaire avec une clef d'une certaine valeur'''
    r = {}
    for i in t :
        if i[key] == value :
            r = i
    return r


def button(rect : tuple, text : str, text_color : tuple, text_size : int, color : tuple, color2 : tuple) -> bool : # Par Victor
    '''Affiche un bouton à rect(gauche, haut, longueur, hauteur),
    du texte, avec couleur et taille, et sa couleur, et renvoie True si il est cliqué.
    Il passe à la couleur de color2 (optionnel) quand la souris est dessus'''
    global mouse_pressed
    
    rleft = rect[0]
    rtop = rect[1]
    rwidth = rect[2]
    rheight = rect[3]
    
    mp = pg.mouse.get_pos()
    mpx = mp[0]
    mpy = mp[1]
    
    if mpx >= rleft*SCALE and mpy >= rtop*SCALE and mpx <= (rleft + rwidth)*SCALE and mpy <= (rtop + rheight)*SCALE :
        pg.draw.rect(surface, color2, (rleft*SCALE, rtop*SCALE, rwidth*SCALE, rheight*SCALE))
        print_txt(text, ((rleft + (rwidth/2)), (rtop + (rheight/2))), text_size, text_color, True)
        if click() : # click gauche
            #print("truc")
            return True
        else :
            return False
                
    else :
        pg.draw.rect(surface, color, (rleft*SCALE, rtop*SCALE, rwidth*SCALE, rheight*SCALE))
        print_txt(text, ((rleft + (rwidth/2)), (rtop + (rheight/2))), text_size, text_color, True)
        return False
    


def level_info(current_level:int)->None:#Kimi
    """Affiche les infos du level"""
    global level_color, difficulty
    pg.draw.rect(surface, LIGHT_GREY, (0, 0, 1200*SCALE, 90*SCALE)) # Bandeau supérieur
    
    if current_level <= 10 :
        difficulty = "Facile"
        level_color = GREEN
    elif current_level <= 20 :
        difficulty = "Normal"
        level_color = YELLOW
    elif current_level <= 30 :
        difficulty = "Difficile"
        level_color = ORANGE
    elif current_level <= 40 :
        difficulty = "Expert"
        level_color = RED
    elif current_level <= 49 :
        difficulty = "Maître"
        level_color = PURPLE
    else :
        difficulty = "Impossible"
        level_color = BLACK
        
    nom = levels_data[current_level-1]['nom']
    f_brute = levels_data[current_level-1]['formule brute']
    print_txt("Niveau " + str(current_level), (1050, 30), 35, BLACK, True)
    print_txt(difficulty, (1050, 65), 30, level_color, True)
    print_txt(str(nom), (600, 30), 35, BLACK, True)
    print_txt(str(f_brute), (600, 65), 30, BLACK, True)


def create_atoms(current_level:int)->list:#victor+kimi
    """Crée chaque atome"""
    atom_list = levels_data[current_level-1]['atomes']
    atom_id_list = ['']*len(atom_list)
    #print(atom_list)
    for i in range(len(atom_list)) :
        valence = find_in_dlist(atoms_data, "symbole", atom_list[i])["valence"]
        atom_id_list[i]={"id" : int(i+1),"name" : str(atom_list[i]), "pos" : ((600 + cos(radians(360/len(atom_list)*i))*350), (450 + sin(radians(360/len(atom_list)*i))*250)), "links": []}
    #print(atom_id_list)
    return atom_id_list


def detect_win() -> bool : # Par Victor
    '''Détecte si le joueur a gagné et renvoie un booléen correspondant
    Détection simple : on vérifie juste que tous les atomes ont le bon nombre de liaisons
    Puis complexe : tous les atomes doivent faire partie de la même chaîne'''
    
    win = True
    # Ouais bon en fait c'est plus une détection de défaite
    
    for a in atoms :
        nb_links = 0
        for i in a["links"] :
            nb_links += i[1] # Compte le nombre de liens de l'atome a
            
        #print(a["name"], nb_links)
        #print("valence", find_in_dlist(atoms_data, "symbole", a["name"])["valence"])
        
        if nb_links != find_in_dlist(atoms_data, "symbole", a["name"])["valence"] : # Quand le nombre de liaisons n'est pas le max
            win = False
    
    
    if win :
        n = len(atoms)
        all_links = [[False for i in range(n)] for i in range(n)]
    
        for i in range(n):
            all_links[i][i] = True
            linked_to_i = get_links_ids(i+1)
            for l in linked_to_i:
                all_links[i][l-1] = True
                all_links[l-1][i] = True
    
        looping = True
        counter = 0
        while looping :
            counter += 1
            for i in range(n):
                for j in range(n):
                    if all_links[i][j] :
                        for k in range(n) :
                            if all_links[j][k] :
                                all_links[i][k] = True
                                all_links[k][i] = True
        
            all_true = True
            for i in range(n):
                for j in range(n):
                    if all_links[i][j] :
                        all_true = False
                    
            if all_true or counter >= n :
                looping = False
        
    
    
        for i in range(n):
            for j in range(n):
                if not all_links[i][j] :
                    win = False
            
    #print(all_links)
    
    
    return win

def get_links_ids(a_id : int) -> list[int] : # Par Victor
    '''Renvoie la liste des id des atomes liés à l'atome ciblé'''
    #print(a_id)
    links = find_in_dlist(atoms, "id", a_id)["links"]
    l = [0 for i in range(len(links))]
    for i in range(len(links)) :
        l[i] = links[i][0]
    return l

def delete_doubles(t : list) -> list : # Par Victor
    '''Supprime en place les doublons d'une liste'''
    copy = []
    for i in t :
        if not i in copy :
            copy.append(i)
    return copy
 
def background(color:tuple) -> None : # Par Victor amélioré par Kimi
    '''Dessine un arrière plan stylé'''
    if bg_on :
        for i in range(6) :
            modifier = 0.2 + i/15
            radius = 350 + i*80
            pt1 = (((600 + cos(radians(90+tick*modifier))*radius), (450 + sin(radians(90+tick*modifier))*radius)))
            pt2 = (((600 + cos(radians(180+tick*modifier))*radius), (450 + sin(radians(180+tick*modifier))*radius)))
            pt3 = (((600 + cos(radians(270+tick*modifier))*radius), (450 + sin(radians(270+tick*modifier))*radius)))
            pt4 = (((600 + cos(radians(tick*modifier))*radius), (450 + sin(radians(tick*modifier))*radius)))
            r=min(color[0]+i*20,255)
            g=min(color[1]+i*20,255)
            b=min(color[2]+i*20,255)
            pg.draw.lines(surface, (r,g,b), True, [scaling(pt1), scaling(pt2), scaling(pt3), scaling(pt4)], int(5*SCALE))

    
    
   


# -----<===== BOUCLE PRINCIPALE =====>-----

# Par Victor

menu = "main"

clock = pg.time.Clock()

running = True

while running :
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False   # Quitte la boucle quand l'évènement QUIT est détecté
    
    
    render()
    pg.display.flip()
    
    
    # ----- TESTS -----
    
    #print(menu)
    #print(pg.mouse.get_pressed())
    #print(levels_data[0]['atomes'][0])
    
    # -----------------
    
    
    tick += 1 # + 1 ticks par frame (60 par seconde)
    clock.tick(60) # Met le FPS à 60
    

print("Fermeture de la fenêtre...")

pg.font.quit()
pg.display.quit()
pg.quit()

print("----------------------------------------")

print("Merci d'avoir joué à notre jeu ! À bientôt pour plus de chimie ;)")




















