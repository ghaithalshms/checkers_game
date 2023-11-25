import tkinter as tk

p = [
    ["PN", "N", "PN", "N", "PN", "N"],
    ["N", "PN", "N", "PN", "N", "PN"],
    ["B", "N", "B", "N", "B", "N"],
    ["N", "B", "N", "B", "N", "B"],
    ["PB", "N", "PB", "N", "PB", "N"],
    ["N", "PB", "N", "PB", "N", "PB"]
]

tourDeJouer = "PB"  # PB pour piosn blancs et PN pour pions noirs, commencer par les blancs

# les pion sont stocké en string comme YX
pionSelectionne = 0

# Créer une liste pour stocker les objets du canevas
canvas_objets = []
lignes = 6
colonnes = 6

# Creer des objets None pour les mettre a jour
for i in range(lignes):
    row = [None] * colonnes
    canvas_objets.append(row)


def button_click(ligne, colonne):
    global pionSelectionne
    global tourDeJouer

    if pionSelectionne == 0:
        # Definir le pion a deplacer s'il y a un pion dans la place
        # aussi si le tour de jouer est pour le pion selectionne
        _couleurDuPionSelectionne = p[int(ligne)][int(
            colonne)]
        if (_couleurDuPionSelectionne == "PB" or _couleurDuPionSelectionne == "PN") and _couleurDuPionSelectionne == tourDeJouer:
            pionSelectionne = str(ligne)+str(colonne)

    else:
        # Faire le deplacement

        # ne pas deplacer s'il y a un pion dans la place a deplacer
        # ou si la place est noire
        couleurDuPionSelectionne = p[int(
            pionSelectionne[0])][int(pionSelectionne[1])]

        nouvellePlace = p[int(
            ligne)][int(colonne)]

        # changer le pion selectionne si le joueur selection son autre pion
        if nouvellePlace == couleurDuPionSelectionne:
            pionSelectionne = str(ligne)+str(colonne)
            return  # sortir de la fonction
        peutDeplacer = False if nouvellePlace == "PB" or nouvellePlace == "PN" or nouvellePlace == "N" else True

        ''' controller la nouvelle place de deplacement (regle de deplacement)
         si le pion peut deja deplacer '''
        if peutDeplacer:
            _ancienPlaceY = int(pionSelectionne[0])
            _ancienPlaceX = int(pionSelectionne[1])
            _nouvellePlaceY = int(ligne)
            _nouvellePlaceX = int(colonne)

            '''un parcours justement au haute pour les pions blancs
            et un parcours justement au bas pour les pions noirs'''
            parcoursY = (_ancienPlaceY)-(_nouvellePlaceY) if couleurDuPionSelectionne == "PB" else (
                _nouvellePlaceY)-(_ancienPlaceY)

            # un parcours a droite (positive) ou a gauche (negative)
            parcoursX = (_ancienPlaceX)-(_nouvellePlaceX)
            parcoursADirection = "D" if parcoursX > 0 else "G"  # D=droite et G=gauche
            parcoursX = abs(parcoursX)  # pour le faire positive

            # le pion peut deplacer s'il a deplace une place haute et une place droite ou gauche
            peutDeplacer = True if (
                parcoursY == 1 and parcoursX == 1) else False

            # s'il a deplace 2 places pour manger:
            # le '\' est ajoute par vscode pour passer a nouvelle ligne
            if (parcoursY == 2 and parcoursX == 2):
                _pionAMangerY = _nouvellePlaceY + \
                    1 if couleurDuPionSelectionne == "PB" else _nouvellePlaceY-1
                _pionAMangerX = _nouvellePlaceX+1 if parcoursADirection == "D" else _nouvellePlaceX-1
                _couleurDuPionAManger = p[_pionAMangerY][_pionAMangerX]

                # detecter le couleur du pion a manger
                if (_couleurDuPionAManger == "PB" or _couleurDuPionAManger == "PN") and _couleurDuPionAManger != couleurDuPionSelectionne:
                    peutDeplacer = True  # faire le deplacement
                    # supprimer le pion mangé
                    p[_pionAMangerY][_pionAMangerX] = "B"
                    canvasDeLaPlaceDuPionMange = canvas_objets[_pionAMangerY][_pionAMangerX]
                    canvasDeLaPlaceDuPionMange.delete("all")

        if peutDeplacer:
            # Acceder a objet canevas de la ancien place
            canvasDuPionSelectionne = canvas_objets[int(
                pionSelectionne[0])][int(pionSelectionne[1])]

            # Acceder a objet canevas de la nouvelle place
            canvasDeLaNouvellePlace = canvas_objets[ligne][colonne]

            # Deplacer le pion a la nouvelle place
            canvasDeLaNouvellePlace.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
                                                circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="white" if couleurDuPionSelectionne == "PB" else "black")

            # Supprimer le pion de la nouvelle place
            canvasDuPionSelectionne.delete("all")

            # Mettre a jour le list de la table
            p[ligne][colonne] = p[int(
                pionSelectionne[0])][int(pionSelectionne[1])]
            p[int(pionSelectionne[0])][int(pionSelectionne[1])] = "B"

            # changer le tour de jouer
            tourDeJouer = "PB" if couleurDuPionSelectionne == "PN" else "PN"

        pionSelectionne = 0


root = tk.Tk()
root.title("Jeu du Dames")

# Creation de 6x6 canvas pour la table du jeu
for y in range(6):
    for x in range(6):
        # c9a3a3 : couleur de blanc
        # 3b2020 : couleur de noir
        color = "#c9a3a3" if (
            y + x) % 2 == 0 else "#3b2020"

        canvas = tk.Canvas(root, height=60, width=60, bg=color)
        canvas.grid(row=y, column=x)

        canvas_objets[y][x] = canvas  # Stocker les canvas

        circle_radius = 20
        circle_center = (30, 30)

        # pions des premieres 2 lignes
        if y in [0, 1] and (y + x) % 2 == 0:
            canvas.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
                               circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="black")

        # pions des dernieres 2 lignes
        if y in [4, 5] and (y + x) % 2 == 0:
            canvas.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
                               circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="white")

        canvas.bind("<Button-1>", lambda event, ligne=y,
                    colonne=x: button_click(ligne, colonne))

root.mainloop()
