#TIC TAC TOE

def welcome():
    print("WELCOME TO MY TIC TAC TOE!")
welcome()

winning_combination = [
    [(0,0), (0,1), (0, 2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2, 2)],
    [(0,2), (1,1), (2,0)],
]
board_matrix = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

game_going = True
current_player = "X"

def display_board():
    print("*****************")
    for board in board_matrix:
        print("--|---|--") # print("*  ""  --|---|--""  *")
        print(" | ".join(board)) # print("*  ""  --|---|--""  *")
    print("--|---|--")
    print("*****************")
        
display_board()

def player_input():  
    row = int(input(f"{current_player} choose a row: ")) 
    column = int(input("Now choose a column: "))
    while board_matrix[row - 1][column - 1] !=  " ":
         print("this position is already taken choose another one")
         continue
    else:
        board_matrix[row - 1][column - 1] = current_player
        display_board()

    
win_combination = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def chek_win():
    #global winner
    for comb in win_combination:
        for position in comb:
            if position == "X":
                print("the winner is 'X'")
            elif position == "O":
                print("the winner is 'O'")
            elif " " not in board_matrix:
                print("No one wins")
                   
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def play():
    while game_going:
        display_board
        player_input()
        chek_win()
    