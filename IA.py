from random import randint
class IA:
    def __init__(self):
        x = 1

    def testAllPossition(self, matrice, turn):
        playablePos = []
        for x in range(8):
            for y in range(8):
                res, count = matrice.testGoodPosition(turn, x, y, False)
                if (res):
                    playablePos.append([[y, x], count])
        return playablePos

    def play(self, matrice, turn):
        playablePos = self.testAllPossition(matrice, turn)
        if (len(playablePos) != 0):

            mouvePlay = self.chooseBestMove(playablePos)
            matrice.testGoodPosition(turn, mouvePlay[1], mouvePlay[0], True)
            matrice.matrice[mouvePlay[1]][mouvePlay[0]] = turn
            return True
        else:
            return False

    def chooseBestMove(self, playablePos):
        my_list = playablePos
        for i in range(len(my_list)):
            count = 100
            count += my_list[i][1]
            col, row = my_list[i][0]
            if row == 0 and col == 0 or row == 7 and col == 7 or row == 7 and col == 0 or row == 0 and col == 7:
                count += 10
            elif row == 0 or row == 7 or col == 0 or col == 7:
                count += 5
            if (col == 1 or col == 6) and (row == 1 or row == 6):
                count -= 100
            my_list[i][1] = count
        my_list = sorted(my_list, key=lambda x: x[1], reverse=True)
        lst_bestMove = [my_list[0]]
        i = 1
        while i < len(my_list) and lst_bestMove[0][1] == my_list[i][1]:
            lst_bestMove.append(my_list[i])
            i += 1

        return lst_bestMove[randint(0, len(lst_bestMove) - 1)][0]
