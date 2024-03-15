import numpy as np

def main():
    board = np.full((8, 9), " ", dtype=str)
    board[3,3] = "1"
    board[4,4] = "1"
    board[3,4] = "2"
    board[4,3] = "2"
    topBoard = np.array(["A","B","C","D","E","F","G","H"," "])
    y = 0
    for x in range(1, 9):
        board[y][8] = x
        y += 1

    totalBoard = np.vstack((topBoard, board), dtype=str)
    
    turn = 0
    while np.any(totalBoard[1:,:8] == " "):
        if turn == 0:
            jeton = "1"
            turn = 1
        else:
            jeton = "2"
            turn = 0
            
        print(totalBoard)
        print(f"Au tour de : {jeton}")
        
        notPlace = True
        while notPlace:
            pos = str(input("Dans quelle case mettre le jeton ?"))
            colone = ord((pos[0]).lower()) - ord('a')
            ligne = int(pos[1]) - 1

            if testGoodPosition(board, jeton, ligne, colone):
                board[ligne,colone] = jeton
                notPlace = False
        
        totalBoard = np.vstack((topBoard, board), dtype=str)
    
def testGoodPosition(board, jeton, ligne, colone):
    possibilite = []
    possibilite.append(verifN(board, jeton, ligne, colone))
    possibilite.append(verifNO(board, jeton, ligne, colone))
    possibilite.append(verifO(board, jeton, ligne, colone))
    possibilite.append(verifSO(board, jeton, ligne, colone))
    possibilite.append(verifS(board, jeton, ligne, colone))
    possibilite.append(verifSE(board, jeton, ligne, colone))
    possibilite.append(verifE(board, jeton, ligne, colone))
    possibilite.append(verifNE(board, jeton, ligne, colone))
    return np.any(possibilite)

def verifE(board, jeton, ligne, colone):
    count = 0
    for i in range(colone+1, 8):
        if board[ligne, i] == " ":
            return False
        elif board[ligne, i] == jeton:
            if count != 0:
                mange(board, 0, 1, ligne, colone, jeton)
                return True
            return False
        else:
            count += 1
    return False

def verifO(board, jeton, ligne, colone):
    count = 0
    for i in range(colone-1, -1, -1):
        if board[ligne, i] == " ":
            return False
        elif board[ligne, i] == jeton:
            if count != 0:
                mange(board, 0, -1, ligne, colone, jeton)
                return True
            return False
        else:
            count += 1
    return False

def verifS(board, jeton, ligne, colone):
    count = 0
    for i in range(ligne+1, 8):
        if board[i, colone] == " ":
            return False
        elif board[i, colone] == jeton:
            if count != 0:
                mange(board, 1, 0, ligne, colone, jeton)
                return True
            return False
        else:
            count += 1
    return False

def verifN(board, jeton, ligne, colone):
    count = 0
    for i in range(ligne-1, -1, -1):
        if board[i, colone] == " ":
            return False
        elif board[i, colone] == jeton:
            if count != 0:
                mange(board, -1, 0, ligne, colone, jeton)
                return True
            return False
        else:
            count += 1
    return False

def verifSE(board, jeton, ligne, colone):
    count = 0
    if ligne > colone:
        max = ligne
    else:
        max = colone
    for i in range(1, 8-max):
        if board[ligne + i, colone + i] == " ":
            return False
        elif board[ligne + i, colone + i] == jeton:
            if count != 0:
                mange(board, 1, 1, ligne, colone, jeton)
                return True
            return False
        else:
            count += 1
    return False

def verifNO(board, jeton, ligne, colone):
    count = 0
    if ligne < colone:
        min = ligne
    else:
        min = colone
    for i in range(1, min):
        if board[ligne - i, colone - i] == " ":
            return False
        elif board[ligne - i, colone - i] == jeton:
            if count != 0:
                mange(board, -1, -1, ligne, colone, jeton)
                return True
            return False
        else:
            count += 1
    return False

def verifNE(board, jeton, ligne, colone):
    count = 0
    tmpColone = (colone + 7) - colone*2
    if ligne > tmpColone:
        max = ligne
    else:
        max = colone
    for i in range(1, 8-max):
        if board[ligne - i, colone + i] == " ":
            return False
        elif board[ligne - i, colone + i] == jeton:
            if count != 0:
                mange(board, -1, 1, ligne, colone, jeton)
                return True
            return False
        else:
            count += 1
    return False

def verifSO(board, jeton, ligne, colone):
    count = 0
    tmpColone = (colone + 7) - colone*2
    if ligne < tmpColone:
        max = ligne
    else:
        max = colone
    for i in range(1, max+1):
        if board[ligne + i, colone - i] == " ":
            return False
        elif board[ligne + i, colone - i] == jeton:
            if count != 0:
                mange(board, 1, -1, ligne, colone, jeton)
                return True
            return False
        else:
            count += 1
    return False

def mange(board, dirLigne, dirColone, ligne, colone, jeton):
    x = ligne + dirLigne
    y = colone + dirColone
    while board[x,y] != jeton:
        board[x,y] = jeton
        x += dirLigne
        y += dirColone

main()