import tkinter as tk

import numpy as np


class Board:
    def __init__(self):
        self.matrice = np.zeros((8, 8))
        self.matrice[3][3] = 1
        self.matrice[4][4] = 1
        self.matrice[3][4] = 2
        self.matrice[4][3] = 2
        print(self.matrice)
        self.fenetre = tk.Tk()
        self.fenetre.geometry('920x820')
        self.fenetre.title('Othello')
        self.Canvas = tk.Canvas(self.fenetre, width=920, height=820)
        self.x_start = 200
        self.y_start = 20
        self.case_size = 700 // 8
        print(self.case_size)
        self.Canvas.pack()
        self.turn = 1
        self.write_board()
        self.update_turn_text()
        n, b = self.count_ones_and_twos()
        self.update_black_pawn(b)
        self.update_white_pawn(n)
        self.Canvas.bind("<Button-1>", self.calc_case)

    def write_board(self):
        self.Canvas.create_rectangle(0, 0, 200, 820, fill="#2f1b0c")  # gauche
        self.Canvas.create_rectangle(200, 717, 920, 820, fill="#2f1b0c")  # Bas
        self.Canvas.create_rectangle(897, 20, 920, 717, fill="#2f1b0c")  # droite
        self.Canvas.create_rectangle(200, 0, 920, 20, fill="#2f1b0c")  # Haut

        for i in range(8):  # 8 rangées
            for j in range(8):  # 8 colonnes
                x0 = self.x_start + j * self.case_size
                y0 = self.y_start + i * self.case_size
                x1 = x0 + self.case_size
                y1 = y0 + self.case_size
                self.Canvas.create_rectangle(x0, y0, x1, y1, fill="#347940")

        x_start = 200 + self.case_size // 2
        y_start = 13
        lst = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(8):
            self.Canvas.create_text(x_start, y_start, text=lst[i], fill="white", font=('Arial', 13))
            x_start += self.case_size

        x_start = 905
        y_start = 20 + self.case_size // 2
        for i in range(8):
            self.Canvas.create_text(x_start, y_start, text=str(i + 1), fill="white", font=('Arial', 15))
            y_start += self.case_size

        self.Canvas.create_text(100, 50, text="Othello", fill="white", font=('Arial', 30))
        self.write_circle(3, 4, "black")
        self.write_circle(3, 3, "white")
        self.write_circle(4, 3, "black")
        self.write_circle(4, 4, "white")
        bouton = tk.Button(self.Canvas, text="passer", command=self.passer)
        bouton.place(x=780, y=750)

    def calc_case(self, event):
        col = (event.x - self.x_start) // self.case_size
        row = (event.y - self.y_start) // self.case_size
        if col >= 0 and row >= 0 and col < 8 and row < 8:
            if self.matrice[row][col] == 0:
                self.matrice[row][col] = self.turn
                print(self.matrice)

                if self.turn == 1:
                    color = 'white'
                    self.turn = 2
                else:
                    color = 'black'
                    self.turn = 1
                print(self.count_ones_and_twos())
                self.update_turn_text()
                self.write_circle(col, row, color)
                n, b = self.count_ones_and_twos()
                self.update_black_pawn(b)
                self.update_white_pawn(n)

    def write_circle(self, col, row, color):
        x_center = self.x_start + col * self.case_size + self.case_size // 2
        y_center = self.y_start + row * self.case_size + self.case_size // 2
        rayon = self.case_size // 2 - 5
        self.Canvas.create_oval(x_center - rayon, y_center - rayon, x_center + rayon, y_center + rayon, fill=color)

    def update_turn_text(self):
        self.Canvas.delete("turn_text")
        player = "Blanc" if self.turn == 1 else "Noir"
        self.Canvas.create_text(560, 765, text=f"Au tour du joueur {player}", fill="white", font=('Arial', 20),
                                tags="turn_text")

    def update_black_pawn(self, nb):
        self.Canvas.delete("black_pawn")
        self.Canvas.create_text(230, 740, text=f"N : {nb}", fill="white", font=('Arial', 15),
                                tags="black_pawn")

    def update_white_pawn(self, nb):
        self.Canvas.delete("white_pawn")
        self.Canvas.create_text(230, 775, text=f"B : {nb}", fill="white", font=('Arial', 15),
                                tags="white_pawn")

    def passer(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
        self.update_turn_text()

    def count_ones_and_twos(self):
        count_ones = np.count_nonzero(self.matrice == 1)
        count_twos = np.count_nonzero(self.matrice == 2)
        return count_ones, count_twos
