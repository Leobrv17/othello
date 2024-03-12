import numpy as np

def main():
    board = np.full((8, 9), " ", dtype=str)
    board[3,3] = "B"
    board[4,4] = "B"
    board[3,4] = "N"
    board[4,3] = "N"
    topBoard = np.array(["A","B","C","D","E","F","G","H"," "])
    y = 0
    for x in range(1, 9):
        board[y][8] = x
        y += 1

    totalBoard = np.vstack((topBoard, board), dtype=str)
    
    turn = 0
    while np.any(totalBoard[1:,:8] == " "):
        if turn == 0:
            jeton = "B"
            turn = 1
        else:
            jeton = "N"
            turn = 0
            
        print(totalBoard)
        print(f"Au tour de : {jeton}")
        
        pos = str(input("Dans quelle case mettre le jeton ?"))
        colone = ord((pos[0]).lower()) - ord('a')
        ligne = int(pos[1]) - 1

        if goodPosition(board, jeton, ligne, colone):
            board[ligne][colone] = jeton
        
        totalBoard = np.vstack((topBoard, board), dtype=str)
    
def goodPosition(board, jeton, ligne, colone):
    return True

main()