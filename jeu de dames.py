import tkinter as tk

p = [
    ["PN", "B", "PN", "B", "PN", "B"],
    ["B", "PN", "B", "PN", "B", "PN"],
    ["N", "B", "N", "B", "N", "B"],
    ["B", "N", "B", "N", "B", "N"],
    ["PB", "B", "PB", "B", "PB", "B"],
    ["B", "PB", "B", "PB", "B", "PB"]
]

pionSelectionne = 0
nouvellePlaceDuPion = 0

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
    global nouvellePlaceDuPion

    if pionSelectionne == 0:
        # Definir le pion a deplacer
        pionSelectionne = str(ligne)+str(colonne)
    else:
        # Faire le deplacement
        ancienePlace = ""  # blanc
        if (ligne + colonne) % 2 == 0:
            ancienePlace = "N"  # noir
        else:
            ancienePlace = "B"  # blanc
        couleurDuPionSelectionne = p[int(
            pionSelectionne[0])][int(pionSelectionne[1])]

        nouvellePlaceDuPion = str(ligne)+str(colonne)

        # Acceder a ancien et nouveau objet du canevas
        canvasDuPionSelectionne = canvas_objets[int(
            pionSelectionne[0])][int(pionSelectionne[1])]

        canvasDeLaNouvellePlace = canvas_objets[ligne][colonne]

        # Deplacer le pion a la nouvelle place
        # SI il y avait deja un pion
        if couleurDuPionSelectionne == "PB" or couleurDuPionSelectionne == "PN":
            canvasDeLaNouvellePlace.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
                                                circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="white" if couleurDuPionSelectionne == "PB" else "black")

        # Remove the oval from the old place
        canvasDuPionSelectionne.delete("all")

        # Update the p list
        p[ligne][colonne] = p[int(pionSelectionne[0])][int(pionSelectionne[1])]
        p[int(pionSelectionne[0])][int(pionSelectionne[1])] = ancienePlace

        pionSelectionne = 0


root = tk.Tk()
root.title("Jeu du Dames")

# Creation de 6x6 canvas pour la table du jeu
for y in range(6):
    for x in range(6):
        color = "#c9a3a3" if (y + x) % 2 == 0 else "#3b2020"

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
