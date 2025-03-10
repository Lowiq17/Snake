from fltk import *
from time import sleep
from random import randint 
def case_vers_pixel(case):
    """
    Reçoit les coordonnées d'une case du plateau sous la forme d'un couple
    d'entiers (ligne, colonne) et renvoie les coordonnées du centre de cette
    case. 
    
    Ce calcul prend en compte la taille de chaque case, donnée par la variable
    globale `taille_case`.

    >>> taille_case = 10
    >>> case_vers_pixel(4, 6)
    (45.0, 65.0)
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case


def affiche_pommes(pommes):
    """
    Dessine une pomme dans chaque case désignée par la liste de couples
    d'entiers `pommes`. Pas de valeur de retour.
    """
    i = 0
    while i < len(pommes):
        pomme = pommes[i]
        x, y = case_vers_pixel(pomme)
        cercle(x, y, taille_case/2,
               couleur='darkred', remplissage='red')
        rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7,
                  couleur='darkgreen', remplissage='darkgreen')
        i += 1
        

def affiche_serpent(serpent):
    """
    Dessine le serpent dont les éléments du corps sont désignés par la liste de
    couples d'entiers `serpent` (le premier élément de la liste désigne la tête
    du serpent). Pas de valeur de retour.
    """
    for i in range(len(serpent)):
        x, y = case_vers_pixel(serpent[i])  # à modifier !!!

        cercle(x, y, taille_case/2 + 1,
               couleur='yellow', remplissage='yellow')


def change_direction(touche):
    """
    Renvoie le vecteur unitaire indiquant la direction correspondant à la touche
    pressée par l'utilisateur. Les valeurs de retour possibles sont `(0, 1)`,
    `(1, 0)`, `(0, -1)` et `(-1, 0)`.
    """
    # à compléter !!!
    if touche == 'Up':
        # flèche haut pressée
        return (0, -1)
    elif touche == 'Down':
        return (0, 1)
    elif touche == 'Right':
        return (1, 0)
    elif touche == 'Left':
        return (-1, 0)
    else:
        # pas de changement !
        return direction


# programme principal
if __name__ == "__main__":
    # dimensions du jeu
    taille_case = 20
    largeur_plateau = 40  # en nombre de cases
    hauteur_plateau = 30  # en nombre de cases

    # initialisation du jeu
    framerate = 10    # taux de rafraîchissement du jeu en images/s
    direction = (0, 0)  # direction initiale du serpent (vecteur)
    pommes = [(randint(1,39),randint(1,29))] # liste des coordonnées des cases contenant des pommes
    serpent = [(0, 0)] # liste des coordonnées de cases adjacentes décrivant le serpent
    cree_fenetre(taille_case * largeur_plateau,
                 taille_case * hauteur_plateau)
    
    # boucle principale
    lst_touches = []
    jouer = True
    while jouer:
        # affichage des objets
        efface_tout()
        image(400, 300, "image3.png", ancrage = 'center')
        
        t = texte(400, 300, "Appuyer sur une direction pour jouer !", ancrage = 'center', taille = 30)
        t1 = texte(400, 350, "Manger les pommes pour grandir", ancrage= 'center', taille = 30)
        affiche_pommes(pommes)   
        
        affiche_serpent(serpent) 
        mise_a_jour()

        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'Quitte':
            jouer = False
        
        elif ty == 'Touche':
           direction = change_direction(touche(ev))
           
          
           
           
           
           
        if len(serpent) > 4 :
            for pas in range(1,len(serpent)) :
                a = len(serpent)-1
                b =len(serpent)-1-pas
                if a != b and serpent[a] == serpent [b] :
                            jouer = False
        
        
        if serpent[len(serpent) - 1] in pommes:
            pommes.remove(serpent[len(serpent) - 1])
            serpent.append(serpent[len(serpent) - 1])
            pommes.append((randint(1,39),randint(1,29)))
        serpent.append((serpent[len(serpent) - 1][0]+direction[0],serpent[len(serpent) - 1][1]+direction[1]))
        serpent.pop(0)
        
        
        
        # attente avant rafraîchissement
        sleep(1/framerate)

    # fermeture et sortie
    ferme_fenetre()



#Problèmes à regler : 1) pas de mort par sortiepour le moment; 2) on peut aller en haut alors qu'on allait en bas etc ...