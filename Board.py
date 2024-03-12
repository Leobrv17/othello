import tkinter as tk


class Board:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.geometry('920x820')
        self.fenetre.title('Othello')
        self.Canvas = tk.Canvas(self.fenetre, width=920, height=820)
        self.x_start = 200
        self.y_start = 20
        self.case_size = 700 // 8
        self.Canvas.pack()
        self.turn = 0
        self.write_board()
        self.update_turn_text()
        self.Canvas.bind("<Button-1>", self.write_circle)

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

    def write_circle(self, event):
        col = (event.x - self.x_start) // self.case_size
        row = (event.y - self.y_start) // self.case_size

        if col >= 0 and row >= 0 and col < 8 and row < 8:
            x_center = self.x_start + col * self.case_size + self.case_size // 2
            y_center = self.y_start + row * self.case_size + self.case_size // 2
            rayon = self.case_size // 2 - 5

            if self.turn == 0:
                color = 'white'
                self.turn = 1
            else:
                color = 'black'
                self.turn = 0
            self.update_turn_text()
            self.Canvas.create_oval(x_center - rayon, y_center - rayon, x_center + rayon, y_center + rayon, fill=color)

    def update_turn_text(self):
        self.Canvas.delete("turn_text")

        player = "Blanc" if self.turn == 0 else "Noir"
        self.Canvas.create_text(560, 765, text=f"Au tour du joueur {player}", fill="white", font=('Arial', 20),
                                tags="turn_text")