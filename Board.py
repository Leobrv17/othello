import tkinter as tk

import numpy as np

from Matrice import Matrice


class MyButton(tk.Button):
    def __init__(self, master, texte, fonction):
        tk.Button.__init__(self)
        self.configure(text=texte, command=fonction)
        self.configure(height=1,
                       width=10,
                       bg='#347940',
                       fg='white',
                       font=('Calibri', 10, 'bold'))


class Board:
    def __init__(self):
        self.my_matrice = Matrice()
        self.turn = 1
        self.fenetre = tk.Tk()
        self.fenetre.geometry('920x820')
        self.fenetre.title('Othello')
        self.Canvas = tk.Canvas(self.fenetre, width=920, height=820)
        self.x_start = 200
        self.y_start = 20
        self.case_size = 700 // 8
        self.Canvas.pack()
        self.write_board()
        self.update_turn_text()
        n, b = self.my_matrice.count_ones_and_twos()
        self.update_black_pawn(b)
        self.update_white_pawn(n)
        self.Canvas.bind("<Button-1>", self.calc_case)
        self.winner = None

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
        bouton_next = MyButton(self.Canvas, "Passer", self.passer)
        bouton_next.place(x=780, y=750)
        bouton_regame = MyButton(self.Canvas, "Rejouer", self.regame)
        bouton_regame.place(x=75, y=700)
        bouton_quit = MyButton(self.Canvas, "Quiter", self.stop)
        bouton_quit.place(x=77, y=750)

    def calc_case(self, event):
        col = (event.x - self.x_start) // self.case_size
        row = (event.y - self.y_start) // self.case_size
        print(row, col)
        if col >= 0 and row >= 0 and col < 8 and row < 8:
            if self.my_matrice.matrice[row][col] == 0 and self.my_matrice.testGoodPosition(self.turn, row, col, True):
                self.my_matrice.matrice[row][col] = self.turn
                print(self.my_matrice.matrice)

                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
                print(self.my_matrice.count_ones_and_twos())
                self.update_turn_text()
                self.new_matrice()
                n, b = self.my_matrice.count_ones_and_twos()
                self.update_black_pawn(b)
                self.update_white_pawn(n)

        if not any(0 in i for i in self.my_matrice.matrice):
            nombre_1 = np.count_nonzero(self.my_matrice.matrice == 1)
            nombre_2 = np.count_nonzero(self.my_matrice.matrice == 2)
            if nombre_1 > nombre_2:
                self.winner = 1
                self.update_text_endgame()
            elif nombre_2 > nombre_1:
                self.winner = 2
                self.update_text_endgame()
            else:
                self.winner = 0
                self.update_text_endgame()
        if not any(1 in i for i in self.my_matrice.matrice):
            self.winner = 2
            self.update_text_endgame()
        if not any(2 in i for i in self.my_matrice.matrice):
            self.winner = 1
            self.update_text_endgame()

    def new_matrice(self):
        self.Canvas.delete("pawn")
        for i in range(8):
            for j in range(8):
                if self.my_matrice.matrice[j, i] != 0:
                    if self.my_matrice.matrice[j, i] == 1:
                        color = 'white'
                        self.write_circle(i, j, color)
                    else:
                        color = 'black'
                        self.write_circle(i, j, color)

    def write_circle(self, col, row, color):
        x_center = self.x_start + col * self.case_size + self.case_size // 2
        y_center = self.y_start + row * self.case_size + self.case_size // 2
        rayon = self.case_size // 2 - 5
        self.Canvas.create_oval(x_center - rayon, y_center - rayon, x_center + rayon, y_center + rayon, fill=color,
                                tags="pawn")

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
        if self.winner == None:
            if self.turn == 1:
                self.turn = 2
            else:
                self.turn = 1
            self.update_turn_text()

    def regame(self):
        self.my_matrice = Matrice()
        self.new_matrice()
        self.turn = 1

    def stop(self):
        self.fenetre.destroy()

    def update_text_endgame(self):
        self.Canvas.delete("turn_text")
        text = "Egalité"
        if self.winner == 1:
            text = "Blanc Gagne"
        elif self.winner == 2:
            text = "Noir Gagne"
        self.Canvas.create_text(560, 765, text=text, fill="white", font=('Arial', 20),
                                tags="turn_text")
