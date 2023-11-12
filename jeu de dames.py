# import tkinter as tk

# class Checkerboard:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Jeu du Dames")
#         self.create_board()

#     def create_board(self):
#         self.circles = {}  # Dictionary to store circle objects and their positions

#         for i in range(6):
#             for j in range(6):
#                 color = "#c9a3a3"
#                 if (i + j) % 2 == 0:
#                     color = "#3b2020"

#                 canvas = tk.Canvas(self.root, height=60, width=60, bg=color)
#                 canvas.grid(row=i, column=j)

#                 if i in [4, 5] and (i + j) % 2 == 0:
#                     circle_radius = 20
#                     circle_center = (30, 30)
#                     circle = canvas.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
#                                                 circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="white")
#                     self.circles[(i, j)] = circle

#                 if i in [0, 1] and (i + j) % 2 == 0:
#                     circle_radius = 20
#                     circle_center = (30, 30)
#                     circle = canvas.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
#                                                 circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="black")
#                     self.circles[(i, j)] = circle

#                 canvas.bind("<Button-1>", lambda event, row=i, col=j: self.button_click(row, col))

#     def button_click(self, row, col):
#         has_circle = (row, col) in self.circles
#         print(f"Button clicked: Row {row}, Column {col}, Has Circle: {has_circle}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     checkerboard = Checkerboard(root)
#     root.mainloop()


import tkinter as tk

p = [
    ["PN", "B", "PN", "B", "PN", "B"],
    ["B", "PN", "B", "PN", "B", "PN"],
    ["N", "B", "N", "B", "N", "B"],
    ["B", "N", "B", "N", "B", "N"],
    ["PB", "B", "PB", "B", "PB", "B"],
    ["B", "PB", "B", "PB", "B", "PB"]
]


def button_click(row, col):
    print(f"Button clicked: Row {row}, Column {col}")


root = tk.Tk()
root.title("Jeu du Dames")

for i in range(6):
    for j in range(6):
        color = "#c9a3a3"
        if (i + j) % 2 == 0:
            color = "#3b2020"

        # Create a Canvas instead of a Button
        canvas = tk.Canvas(root, height=60, width=60, bg=color)
        canvas.grid(row=i, column=j)

        # Draw a circle in the middle of the canvas
        if i in [4, 5] and (i + j) % 2 == 0:
            circle_radius = 20
            circle_center = (30, 30)
            canvas.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
                               circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="white")

        if i in [0, 1] and (i + j) % 2 == 0:
            circle_radius = 20
            circle_center = (30, 30)
            canvas.create_oval(circle_center[0]-circle_radius, circle_center[1]-circle_radius,
                               circle_center[0]+circle_radius, circle_center[1]+circle_radius, fill="black")

        # Attach the button_click function to the Canvas
        canvas.bind("<Button-1>", lambda event, row=i,
                    col=j: button_click(row, col))

root.mainloop()
