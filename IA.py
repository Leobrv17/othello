from random import randint


class IA:
    def __init__(self):
        x = 1

    def testAllPossition(self, matrice, turn):
        playablePos = []
        for x in range(8):
            for y in range(8):
                if (matrice.matrice[y, x] == 0 and matrice.testGoodPosition(turn, x, y, False)):
                    playablePos.append([y, x])
        print(playablePos)
        return playablePos

    def play(self, matrice, turn):
        playablePos = self.testAllPossition(matrice, turn)
        mouvePlay = playablePos[randint(0, len(playablePos)-1)]
        matrice.testGoodPosition(turn, mouvePlay[1], mouvePlay[0], True)
        matrice.matrice[mouvePlay[1]][mouvePlay[0]] = turn
