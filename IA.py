from random import randint


class IA:
    def __init__(self):
        x = 1

    def testAllPossition(self, matrice, turn):
        playablePos = []
        for x in range(8):
            for y in range(8):
                if (matrice.testGoodPosition(turn, x, y, False)):
                    playablePos.append([y, x])
        print(playablePos)
        return playablePos

    def play(self, matrice, turn):
        playablePos = self.testAllPossition(matrice, turn)
        if (len(playablePos) !=0) :
            mouvePlay = playablePos[randint(0, len(playablePos) - 1)]
            matrice.testGoodPosition(turn, mouvePlay[1], mouvePlay[0], True)
            matrice.matrice[mouvePlay[1]][mouvePlay[0]] = turn
            return True
        else:
            return False
