import math

def createBoard(grid):
    board =[]
    for x in range(grid ** 2):
        board.append(x + 1)
    return board

def printBoard(board):
    count1 = 0
    line = ""
    width = int(math.sqrt(len(board)))
    for i in range(width - 1):
        line += "-+"
    line += "-"
    for x in range(width):
        level = width * x
        squares = ""
        count2 = 0
        for y in range(width):
            if (count2 < width - 1):
                squares += f"{board[y + level]}|"
                count2 += 1
            else:
                squares += f"{board[y + level]}"
        print(squares)
        if (count1 < width - 1):
            print(line)
            count1 += 1

def checkWin(board):
    width = math.sqrt(len(board))
    checker = 0
    win = True
    for x in range (width):
        for y in range(1, width):
            if (board[checker] != board[checker + y]):
                win = False
                break
        checker += width
    checker = 0
    for x in range(width):
        for y in range(1, width):
            if (board[checker] != board[checker + (width * y)]):
                win = False
                break
        checker += 1
    return win


def main():

    grid = input('Please enter the size of the game you would like(3-6): ')
    board = createBoard(int(grid))
    printBoard(board)

if __name__ == "__main__":
    main()

