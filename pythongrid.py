from random import randint

battleship_Board = []

def buildBoard():
    for i in range(0,5):
        battleship_Board.append(["0"]*5)

def print_board(battleship_Board):
    for row in battleship_Board:
        print("".join(row))

def setShip(battleship_Board):
    ship_row = randint(0, len(battleship_Board[0]) - 1)
    ship_col = randint(0, len(battleship_Board[0]) - 1)
    return ship_row, ship_col

def getRow_Col():
    guess_row, guess_col = int(input("Guess Row: ")), int(input("Guess Col: "))
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print("Whoa! That's not even the ocean my guy, try again.")
        return getRow_Col()
    elif(battleship_Board[guess_row][guess_col] == "X"):
        print("You already guessed this one, try again.")
        return getRow_Col()
    else:
        row = guess_row
        col = guess_col
        return row, col


def startGame():
    buildBoard()
    print_board(battleship_Board)
    ship_row, ship_col = setShip(battleship_Board)
    sank = 0
    turn = 0
    while turn < 4:
        print("Turn: " + str(turn))
        print("Ships Sank: " + str(sank))
        guess_row, guess_col = getRow_Col()
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations you sank my battleship!")
            sank += 1
            print("Ships Sank: " + str(sank))
            print("Game over! You won.")
            break
        else:
            turn += 1
            print("You missed my battleship!")
            battleship_Board[guess_row][guess_col] = "X"
            print_board(battleship_Board)
            if turn == 4 and sank < 1:
                    print("Game over!")
                    print("You lost!")               
startGame()
