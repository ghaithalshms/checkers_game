# import tkinter as tk

# p = [
#     ["PN", "B", "PN", "B", "PN", "B"],
#     ["B", "PN", "B", "PN", "B", "PN"],
#     ["N", "B", "N", "B", "N", "B"],
#     ["B", "N", "B", "N", "B", "N"],
#     ["PB", "B", "PB", "B", "PB", "B"],
#     ["B", "PB", "B", "PB", "B", "PB"]
# ]

# pionSelectionne = 0
# nouvellePlaceDuPion = 0


# def button_click(row, col):
#     global pionSelectionne
#     global nouvellePlaceDuPion
#     if pionSelectionne == 0:
#         pionSelectionne = str(row)+str(col)
#     else:  # Faire le deplacement
#         ancienePlace = "B"  # blanc
#         if (y + x) % 2 == 0:  # (0;0)=>noir, (0;1)=>blanc, (1;0)=>blanc, (1;1)=> noir
#             ancienePlace = "N"  # noir
#         nouvellePlaceDuPion = str(row)+str(col)
#         # changer la nouvelle place par le pion selectionne
#         p[row][col] = p[int(pionSelectionne[0])][int(pionSelectionne[1])]
#         # effacer le pion de la place ancienne
#         p[int(pionSelectionne[0])][int(pionSelectionne[1])] = ancienePlace
#         pionSelectionne = 0


# root = tk.Tk()
# root.title("Jeu du Dames")

# # Creation de 6x6 canvas pour la table du jeu
# for y in range(6):
#     for x in range(6):
#         color = "#c9a3a3"  # blanc
#         if (y + x) % 2 == 0:  # (0;0)=>noir, (0;1)=>blanc, (1;0)=>blanc, (1;1)=> noir
#             color = "#3b2020"  # noir

#         canvas = tk.Canvas(root, height=60, width=60, bg=color)
#         canvas.grid(row=y, column=x)

#         # Dessiner un cercle au milieu du Canvas
#         if y in [4, 5] and (y + x) % 2 == 0:
#             circle_radius = 20
#             circle_center = (30, 30)
#             canvas.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
#                                circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="white")

#         if y in [0, 1] and (y + x) % 2 == 0:
#             circle_radius = 20
#             circle_center = (30, 30)
#             canvas.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
#                                circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="black")

#         # Attacher la fonction button_click au canvas
#         canvas.bind("<Button-1>", lambda event, row=y,
#                     col=x: button_click(row, col))

# root.mainloop()


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

# Create a two-dimensional list to store canvas objects
canvas_objects = [[None for _ in range(6)] for _ in range(6)]


def button_click(row, col):
    global pionSelectionne
    global nouvellePlaceDuPion

    if pionSelectionne == 0:
        pionSelectionne = str(row)+str(col)
    else:  # Faire le deplacement
        ancienePlace = "B"  # blanc
        if (y + x) % 2 == 0:
            ancienePlace = "N"  # noir
        couleurDuPionSelectionne = p[int(
            pionSelectionne[0])][int(pionSelectionne[1])]

        nouvellePlaceDuPion = str(row)+str(col)

        # Access the old and new canvas objects
        old_canvas = canvas_objects[int(
            pionSelectionne[0])][int(pionSelectionne[1])]
        new_canvas = canvas_objects[row][col]

        # Move the oval to the new place
        new_canvas.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
                               circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="white" if couleurDuPionSelectionne == "PB" else "black")

        # Remove the oval from the old place
        old_canvas.delete("all")

        # Update the p list
        p[row][col] = p[int(pionSelectionne[0])][int(pionSelectionne[1])]
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

        canvas_objects[y][x] = canvas  # Store the canvas object

        if y in [4, 5] and (y + x) % 2 == 0:
            circle_radius = 20
            circle_center = (30, 30)
            canvas.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
                               circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="white")

        if y in [0, 1] and (y + x) % 2 == 0:
            circle_radius = 20
            circle_center = (30, 30)
            canvas.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
                               circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="black")

        canvas.bind("<Button-1>", lambda event, row=y,
                    col=x: button_click(row, col))

root.mainloop()
