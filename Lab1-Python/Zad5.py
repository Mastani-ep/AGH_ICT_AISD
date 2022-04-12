from random import randint


# funkcja wyswietlajaca tablice
def display(board):
    print("-------------")
    j = 0
    for x in range(3):
        print("|", board[j], "|", board[j+1], "|", board[j+2], "|")
        j += 3
        print("-------------")


# funkcja sprawdzajaca
def check(board):
    a = False
    if board[0] == board[1] == board[2] == "X":
        print("Player X won!")
        a = True
    elif board[3] == board[4] == board[5] == "X":
        print("Player X won!")
        a = True
    elif board[6] == board[7] == board[8] == "X":
        print("Player X won!")
        a = True
    elif board[0] == board[3] == board[6] == "X":
        print("Player X won!")
        a = True
    elif board[1] == board[4] == board[7] == "X":
        print("Player X won!")
        a = True
    elif board[2] == board[5] == board[8] == "X":
        print("Player X won!")
        a = True
    elif board[0] == board[4] == board[8] == "X":
        print("Player X won!")
        a = True
    elif board[2] == board[4] == board[6] == "X":
        print("Player X won!")
        a = True
    elif board[0] == board[1] == board[2] == "O":
        print("Player O won!")
        a = True
    elif board[3] == board[4] == board[5] == "O":
        print("Player O won!")
        a = True
    elif board[6] == board[7] == board[8] == "O":
        print("Player O won!")
        a = True
    elif board[0] == board[3] == board[6] == "O":
        print("Player O won!")
        a = True
    elif board[1] == board[4] == board[7] == "O":
        print("Player O won!")
        a = True
    elif board[2] == board[5] == board[8] == "O":
        print("Player O won!")
        a = True
    elif board[0] == board[4] == board[8] == "O":
        print("Player O won!")
        a = True
    elif board[2] == board[4] == board[6] == "O":
        print("Player O won!")
        a = True
    return a


# funkcja wyboru uzytkownika
def choice(board, x):
    k = 1
    if x == 1:
        while k > 0:
            print("Player X, it's your turn: ")
            try:
                z = int(input())
                if board[z] == "O" or board[z] == "X":
                    print("This place is taken")
                else:
                    board[z] = "X"
                    display(board)
                    k = 0
            except ValueError:
                print("Enter a number")
            except IndexError:
                print("Enter a number from 0 to 8")

    if x == 0:
        while k > 0:
            print("Player O, it's your turn: ")
            try:
                z = int(input())
                if board[z] == "O" or board[z] == "X":
                    print("This place is taken")
                else:
                    board[z] = "O"
                    display(board)
                    k = 0
            except ValueError:
                print("Enter a number")
            except IndexError:
                print("Enter a number from 0 to 8")


# funkcja wyboru dla gry z komputerem
def choice_k(board, x):
    k = 1
    if x == 1:
        while k > 0:
            print("Player X, it's your turn: ")
            try:
                z = int(input())
                if board[z] == "O" or board[z] == "X":
                    print("This place is taken")
                else:
                    board[z] = "X"
                    display(board)
                    k = 0
            except ValueError:
                print("Enter a number")
            except IndexError:
                print("Enter a number from 0 to 8")

    if x == 0:
        print("Computer's turn")
        while k > 0:
            z = randint(0, 8)
            if board[z] == "O" or board[z] == "X":
                pass
            else:
                board[z] = "O"
                display(board)
                k = 0


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
l = 0
t = 1
while t > 0:
    print("2 Players(1) or a game with computer?(2) ")
    try:
        f = int(input())
        if f < 1 or f > 2:
            print("Enter a number 1 or 2")
        else:
            t = 0
    except ValueError:
        print("Enter a number 1 or 2")

display(board)
print("Choose a square by entering a number from 0 (upper left corner) to 8 (bottom right corner).")

if f == 1:
    for j in range(5):
        choice(board, 1)
        k = check(board)
        l += 1
        if k == 1:
            break
        if l == 9:
            print("Nobody won :(")
        choice(board, 0)
        k = check(board)
        l+=1
        if k == 1:
            break

if f == 2:
    for j in range(5):
        choice_k(board, 1)
        k = check(board)
        l += 1
        if k == 1:
            break
        if l == 9:
            print("Nobody won :(")
        choice_k(board, 0)
        k = check(board)
        l += 1
        if k == 1:
            break
