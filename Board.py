import tkinter as tk


class Board:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.geometry('920x820')
        self.fenetre.title('Othello')
        self.menu = tk.Canvas(self.fenetre, width=920, height=820)
        self.menu.pack()
        self.write_board()

    def write_board(self):
        self.menu.create_rectangle(0, 0, 200, 820, fill="#2f1b0c")  # gauche
        self.menu.create_rectangle(200, 717, 920, 820, fill="#2f1b0c")  # Bas
        self.menu.create_rectangle(897, 20, 920, 717, fill="#2f1b0c")  # droite
        self.menu.create_rectangle(200, 0, 920, 20, fill="#2f1b0c")  # Haut
        x_start = 200
        y_start = 20
        case_size = 700 // 8

        for i in range(8):  # 8 rangées
            for j in range(8):  # 8 colonnes
                x0 = x_start + j * case_size
                y0 = y_start + i * case_size
                x1 = x0 + case_size
                y1 = y0 + case_size
                self.menu.create_rectangle(x0, y0, x1, y1, fill="#347940")

        x_start = 200 + case_size // 2
        y_start = 13
        lst = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(8):
            self.menu.create_text(x_start, y_start, text=lst[i], fill="white", font=('Arial', 13))
            x_start += case_size

        x_start = 905
        y_start = 20 + case_size // 2
        for i in range(8):
            self.menu.create_text(x_start, y_start, text=str(i + 1), fill="white", font=('Arial', 15))
            y_start += case_size

        self.menu.create_text(100, 50, text="Othello", fill="white", font=('Arial', 30))
