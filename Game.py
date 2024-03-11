from Board import *


class Game:
    def __init__(self):
        self.plateau = Board()

    def run(self):
        self.plateau.fenetre.mainloop()
