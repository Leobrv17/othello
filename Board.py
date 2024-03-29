import tkinter as tk

import numpy as np


class Board:
    def __init__(self):
        self.init_matrices()
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
        bouton_next = tk.Button(self.Canvas, text="passer", command=self.passer)
        bouton_next.place(x=780, y=750)
        bouton_regame = tk.Button(self.Canvas, text="Rejouer", command=self.regame)
        bouton_regame.place(x=75, y=700)
        bouton_quit = tk.Button(self.Canvas, text="Quiter", command=self.stop)
        bouton_quit.place(x=77, y=750)

    def calc_case(self, event):
        col = (event.x - self.x_start) // self.case_size
        row = (event.y - self.y_start) // self.case_size
        print(row, col)
        if col >= 0 and row >= 0 and col < 8 and row < 8:
            if self.matrice[row][col] == 0 and self.testGoodPosition(self.matrice, self.turn, row, col,True):
                self.matrice[row][col] = self.turn
                print(self.matrice)

                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
                print(self.count_ones_and_twos())
                self.update_turn_text()
                self.new_matrice()
                n, b = self.count_ones_and_twos()
                self.update_black_pawn(b)
                self.update_white_pawn(n)

                playablePos = []
                for x in range(8):
                    for y in range(8):
                        if (self.matrice[y, x] == 0 and self.testGoodPosition(self.matrice, self.turn, x, y, False)):
                            playablePos.append([y, x])
                print(playablePos)

        if not any(0 in i for i in self.matrice):
            nombre_1 = np.count_nonzero(self.matrice == 1)
            nombre_2 = np.count_nonzero(self.matrice == 2)
            if nombre_1 > nombre_2:
                self.winner = 1
                self.update_text_endgame()
            elif nombre_2 > nombre_1:
                self.winner = 2
                self.update_text_endgame()
            else:
                self.winner = 0
                self.update_text_endgame()
        if not any(1 in i for i in self.matrice):
            self.winner = 2
            self.update_text_endgame()
        if not any(2 in i for i in self.matrice):
            self.winner = 1
            self.update_text_endgame()

    def new_matrice(self):
        self.Canvas.delete("pawn")
        for i in range(8):
            for j in range(8):
                if self.matrice[j, i] != 0:
                    if self.matrice[j, i] == 1:
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
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
        self.update_turn_text()

    def count_ones_and_twos(self):
        count_ones = np.count_nonzero(self.matrice == 1)
        count_twos = np.count_nonzero(self.matrice == 2)
        return count_ones, count_twos

    def testGoodPosition(self, board, jeton, ligne, colone, doEat):
        possibilite = []
        possibilite.append(self.verifN(board, jeton, ligne, colone, doEat))
        possibilite.append(self.verifNO(board, jeton, ligne, colone, doEat))
        possibilite.append(self.verifO(board, jeton, ligne, colone, doEat))
        possibilite.append(self.verifSO(board, jeton, ligne, colone, doEat))
        possibilite.append(self.verifS(board, jeton, ligne, colone, doEat))
        possibilite.append(self.verifSE(board, jeton, ligne, colone, doEat))
        possibilite.append(self.verifE(board, jeton, ligne, colone, doEat))
        possibilite.append(self.verifNE(board, jeton, ligne, colone, doEat))
        count = sum(sub_array[1] for sub_array in possibilite)
        if (ligne == 0 and colone == 0 or ligne == 7 and colone == 7 or ligne == 7 and colone == 0 or ligne == 0 and colone == 7):
            count += 20
        elif(ligne == 0 or ligne == 7 or colone == 0 or colone == 7):
            count += 5
        return np.any(possibilite)

    def verifE(self, board, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            for i in range(colone + 1, 8):
                if board[ligne, i] == 0:
                    return [False, 0]
                elif board[ligne, i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(board, 0, 1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifO(self, board, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            for i in range(colone - 1, -1, -1):
                if board[ligne, i] == 0:
                    return [False, 0]
                elif board[ligne, i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(board, 0, -1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifS(self, board, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            for i in range(ligne + 1, 8):
                if board[i, colone] == 0:
                    return [False, 0]
                elif board[i, colone] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(board, 1, 0, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifN(self, board, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            for i in range(ligne - 1, -1, -1):
                if board[i, colone] == 0:
                    return [False, 0]
                elif board[i, colone] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(board, -1, 0, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifSE(self, board, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            if ligne > colone:
                max = ligne
            else:
                max = colone
            for i in range(1, 8 - max):
                if board[ligne + i, colone + i] == 0:
                    return [False, 0]
                elif board[ligne + i, colone + i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(board, 1, 1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifNO(self, board, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            if ligne < colone:
                min = ligne
            else:
                min = colone
            for i in range(1, min):
                if board[ligne - i, colone - i] == 0:
                    return [False, 0]
                elif board[ligne - i, colone - i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(board, -1, -1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifSO(self, board, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            if ligne < 7 - colone:
                min = ligne
            else:
                min = 7 - colone
            for i in range(1, min+1):
                if colone + i == 8:
                    return [False, 0]
                if board[ligne - i, colone + i] == 0:
                    return [False, 0]
                elif board[ligne - i, colone + i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(board, -1, 1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifNE(self, board, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            if 7 - ligne < colone:
                min = 7 - ligne
            else:
                min = colone
            for i in range(1, min + 1):
                if ligne + i == 8:
                    return [False, 0]
                if board[ligne + i, colone - i] == 0:
                    return [False, 0]
                elif board[ligne + i, colone - i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(board, 1, -1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def mange(self, board, dirLigne, dirColone, ligne, colone, jeton):
        x = ligne + dirLigne
        y = colone + dirColone
        while board[x, y] != jeton:
            board[x, y] = jeton
            x += dirLigne
            y += dirColone

    def regame(self):
        self.init_matrices()
        self.new_matrice()

    def stop(self):
        self.fenetre.destroy()

    def init_matrices(self):
        self.matrice = np.zeros((8, 8))
        self.matrice[3][3] = 1
        self.matrice[4][4] = 1
        self.matrice[3][4] = 2
        self.matrice[4][3] = 2
        self.turn = 1
        playablePos = []
        for x in range(8):
            for y in range(8):
                if (self.matrice[y, x] == 0 and self.testGoodPosition(self.matrice, self.turn, x, y, False)):
                    playablePos.append([x, y])
        print(playablePos)
        print(self.matrice)