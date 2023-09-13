#TIC TAC TOE

def welcome():
    print("WELCOME TO MY TIC TAC TOE!")
welcome()



board_matrix = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# game_going = True
# current_player = "X"

def display_board():
    print("*****************")
    for board in board_matrix:
        print("--|---|--") # print("*  ""  --|---|--""  *")
        print(" | ".join(board)) # print("*  ""  --|---|--""  *")
    print("--|---|--")
    print("*****************")
        


def player_input(player):  
    row = int(input(f"{player} choose a row: ")) 
    column = int(input("Now choose a column: "))
    while board_matrix[row - 1][column - 1] !=  " ":
         print("this position is already taken choose another one")
         continue
    else:
        board_matrix[row - 1][column - 1] = player
        display_board()


def chek_win():
    win_combination = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]] 
    #global winner
    lst_player = ["X", "O"]
    
    for player in lst_player:
        for comb in win_combination:
            counter = 0
            for position in comb:
                if board_matrix[position[0]][position[1]] == player:
                    counter += 1
                else:
                    break
            if counter == 3:
                print(f'the winner is {player}')
                return True
    position_counter = 0
    for row in board_matrix:
        for pos in row:
            if pos != " ":
                position_counter += 1
    if position_counter == 9:
        print("ex aequo")
        return True


def play():
    while True:
        display_board()
        player_input("X")
        if chek_win() == True:
            break
        player_input("O")
        if chek_win() == True:
            break
play()
    
    
