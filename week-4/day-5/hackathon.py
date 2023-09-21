from random import randint

Hidden_Pattern = [[' ']*8 for x in range(8)]
Guess_Pattern = [[' ']*8 for x in range(8)]
player_pattern = [[' ']*8 for x in range(8)]

let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
list_column = 'ABCDEFGH'


def print_board(board):
    print(' A B C D E F G H')
    print(' ***************')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1


def create_player_ships(board):
    for _ in range(3):
        ship_counter = 1 
        player_ship_row = int(input(f'Please choose a row for your {ship_counter} ship (1-8) '))
        while player_ship_row not in '12345678':
            print("You have to choose a number between 1-8")
            player_ship_row = int(input("Please enter a number from 1 to 8 "))
            
        player_ship_col = input(f'Please choose a column for your ship {ship_counter} (A-H) ').upper()        
        while player_ship_col not in list_column:
                print("You have to choose a letter from A-H")
                player_ship_col = input("Please enter a letter from A to H ").upper()
            
        for i, col in enumerate(list_column):
            if col == player_ship_col:
                player_ship1_col_idx = i
                break
            
        while board[player_ship_row][player_ship1_col_idx] == 'X':-----------------------------
            print('This palce is already taken choose another one')
        board[player_ship_row][player_ship_col] = 'X'
        print_board(board)
        ship_counter += 1
        
    print("Your ships are all set! You are ready to start the game")


def guess_ship_location():
    #Enter the row number between 1 to 8
    guess_row = input(int('Try to guess where your adversair place his boats. Enter a row (1-8) '))
    while guess_row not in '12345678':
        print("Please enter a valid row ")
        guess_row = input('Please enter a number from 1 to 8 ')
        
    #Enter the Ship column from A TO H
    guess_column = input('Please enter a column (A-H) ').upper()
    while guess_column not in 'ABCDEFGH':
        print("Please enter a valid column ")
        guess_column = input('Please enter a letter from A to H ')
        
    for i, col in enumerate(list_column):
        if col == guess_column:
            guess_column_idx = i
            break
    return guess_row - 1, guess_column_idx 


#Function that creates the ships
def create_computer_ships(board):
    for _ in range(3):
        ship_r, ship_cl = randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] == 'X':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = 'X'


def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_ships(Hidden_Pattern)
#print_board(Hidden_Pattern)
turns = 10
while turns > 0:
    print('Welcome to Battleship')
    print_board(Guess_Pattern)
    row,column =guess_ship_location()
    if Guess_Pattern[row][column] == '-':
        print(' You already guessed that ')
    elif Hidden_Pattern[row][column] =='X':
        print(' Congratulations you have hit the battleship ')
        Guess_Pattern[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry,You missed')
        Guess_Pattern[row][column] = '-'
        turns -= 1
    if  count_hit_ships(Guess_Pattern) == 5:
        print("Congratulations you have sunk all the battleships ")
        break
    print(' You have ' +str(turns) + ' turns remaining ')
    if turns == 0:
        print('Game Over ')
        break