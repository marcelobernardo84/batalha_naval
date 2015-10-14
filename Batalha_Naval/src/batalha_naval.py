# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Vamos jogar Batalha Naval!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Tudo a partir daqui deve ir dentro do laco!
# Tenha certeza de recuar quatro espacos!
for turn in range(4):
    guess_row = int(raw_input("Adivinhe a Linha:"))
    guess_col = int(raw_input("Adivinhe a Coluna:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Parabens, voce afundou meu couracado!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, isso nao e nem mesmo no oceano."            
        elif(board[guess_row][guess_col] == "X"):
            print "Joce ja tentou esse."
        else:
            print "Voce errou meu couracado!"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"
            board[ship_row][ship_col] = "T"
            print_board(board)
            break
    # Exiba aqui (turn + 1)!
    print "Turn: " + str(turn + 1)
    print_board(board)