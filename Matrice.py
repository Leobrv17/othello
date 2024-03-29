import numpy as np


class Matrice:
    def __init__(self):
        self.matrice = np.zeros((8, 8))
        self.matrice[3][3] = 1
        self.matrice[4][4] = 1
        self.matrice[3][4] = 2
        self.matrice[4][3] = 2
        self.turn = 1
        playablePos = []

    def count_ones_and_twos(self):
        count_ones = np.count_nonzero(self.matrice == 1)
        count_twos = np.count_nonzero(self.matrice == 2)
        return count_ones, count_twos

    def testGoodPosition(self, jeton, ligne, colone, doEat):
        possibilite = []
        possibilite.append(self.verifN(jeton, ligne, colone, doEat))
        possibilite.append(self.verifNO(jeton, ligne, colone, doEat))
        possibilite.append(self.verifO(jeton, ligne, colone, doEat))
        possibilite.append(self.verifSO(jeton, ligne, colone, doEat))
        possibilite.append(self.verifS(jeton, ligne, colone, doEat))
        possibilite.append(self.verifSE(jeton, ligne, colone, doEat))
        possibilite.append(self.verifE(jeton, ligne, colone, doEat))
        possibilite.append(self.verifNE(jeton, ligne, colone, doEat))
        count = sum(sub_array[1] for sub_array in possibilite)
        if (
                ligne == 0 and colone == 0 or ligne == 7 and colone == 7 or ligne == 7 and colone == 0 or ligne == 0 and colone == 7):
            count += 20
        elif (ligne == 0 or ligne == 7 or colone == 0 or colone == 7):
            count += 5
        return np.any(possibilite)

    def verifE(self, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            for i in range(colone + 1, 8):
                if self.matrice[ligne, i] == 0:
                    return [False, 0]
                elif self.matrice[ligne, i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(0, 1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifO(self, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            for i in range(colone - 1, -1, -1):
                if self.matrice[ligne, i] == 0:
                    return [False, 0]
                elif self.matrice[ligne, i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(0, -1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifS(self, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            for i in range(ligne + 1, 8):
                if self.matrice[i, colone] == 0:
                    return [False, 0]
                elif self.matrice[i, colone] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(1, 0, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifN(self, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            for i in range(ligne - 1, -1, -1):
                if self.matrice[i, colone] == 0:
                    return [False, 0]
                elif self.matrice[i, colone] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(-1, 0, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifSE(self, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            if ligne > colone:
                max = ligne
            else:
                max = colone
            for i in range(1, 8 - max):
                if self.matrice[ligne + i, colone + i] == 0:
                    return [False, 0]
                elif self.matrice[ligne + i, colone + i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(1, 1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifNO(self, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            if ligne < colone:
                min = ligne
            else:
                min = colone
            for i in range(1, min):
                if self.matrice[ligne - i, colone - i] == 0:
                    return [False, 0]
                elif self.matrice[ligne - i, colone - i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(-1, -1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifSO(self, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            if ligne < 7 - colone:
                min = ligne
            else:
                min = 7 - colone
            for i in range(1, min + 1):
                if colone + i == 8:
                    return [False, 0]
                if self.matrice[ligne - i, colone + i] == 0:
                    return [False, 0]
                elif self.matrice[ligne - i, colone + i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(-1, 1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def verifNE(self, jeton, ligne, colone, doEat):
        count = 0
        if (self.matrice[ligne, colone] == 0):
            if 7 - ligne < colone:
                min = 7 - ligne
            else:
                min = colone
            for i in range(1, min + 1):
                if ligne + i == 8:
                    return [False, 0]
                if self.matrice[ligne + i, colone - i] == 0:
                    return [False, 0]
                elif self.matrice[ligne + i, colone - i] == jeton:
                    if count != 0:
                        if doEat:
                            self.mange(1, -1, ligne, colone, jeton)
                        return [True, count]
                    return [False, 0]
                else:
                    count += 1
        return [False, 0]

    def mange(self, dirLigne, dirColone, ligne, colone, jeton):
        x = ligne + dirLigne
        y = colone + dirColone
        while self.matrice[x, y] != jeton:
            self.matrice[x, y] = jeton
            x += dirLigne
            y += dirColone

    def afficher(self):
        print(self.matrice)
