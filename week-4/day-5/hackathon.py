import random
# #Modules to import
# import pygame

# #Initialize modules
# pygame.init()

# #Game settings and variables
# SCREEN_WIDTH = 860
# SCREEN_HEIGHT = 660
# ROWS = 10
# COLOMN = 10
# CELL_SIZE = 50

# #Colors

# #Pygame display intialization 
# GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('BATTLE SHIP')


# #loading game variables
# player_game_logic = 



# #Main game loop
# RUN_GAME = True
# while RUN_GAME:
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUN_GAME = False
    
#     pygame.display.update()
    
# pygame.quit()

computer_board = [['_']*9 for x in range(9)]
player_guess_board = [['_']*9 for x in range(9)]
player_board = [['_']*9 for x in range(9)]

let_to_num = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7} #--------------------------------------
list_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
list_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]


#print board for the right player
def print_board(board):
    print('  A B C D E F G H I')
    row_num = 1
    for row in board:
        print("%s|%s|" % (row_num, "|".join(row))) #--------------------------
        row_num += 1


#create ship for the player
def create_player_ships(board):       
    ship_counter = 1 
    print_board(board)
    for _ in range(5):
        try:
            player_ship_row = int(input(f'Please choose a row for your {ship_counter} ship (1-9) '))
            while player_ship_row not in list_row:
                player_ship_row = int(input("You have to choose a number between 1-9 "))
        except: #---------------------------------------------
            player_ship_row = int(input("You have to choose a number between 1-9 "))
            
        player_ship_col = input(f'Please choose a column for your {ship_counter} ship d(A-I) ').upper()        
        while player_ship_col not in list_column:
            player_ship_col = input("You have to choose a letter from A-I ").upper()
        
        for i, col in enumerate(list_column):
            if col == player_ship_col:
                player_ship_col_idx = i
                break
            
        while board[player_ship_row - 1][player_ship_col_idx] == 'X': #---------------------------
            print('This palce is already taken choose another one')
            
            
        board[player_ship_row - 1][player_ship_col_idx] = 'X'
        ship_counter += 1 
        
        
    print("Your ships are all set! You are ready to start the game")
    print_board(board)


#create ship for the computer
def create_computer_ships(board):
    for _ in range(5):
        ship_r, ship_cl = random.randint(0, 7), random.randint(0, 7)
        while board[ship_r][ship_cl] == 'X':
            ship_r, ship_cl = random.randint(0, 7), random.randint(0, 7)
        board[ship_r][ship_cl] = 'X'
    print("your adversair choose his places")


def player_guess_ship_location():
    guess_row = input(int('Try to guess where your adversair place his boats. Enter a row (1-9) '))
    while guess_row not in list_row:
        guess_row = input(int("Please enter a valid row, a number from 1 to 9 "))
        
    guess_column = input('Please enter a column (A-I) ').upper()
    while guess_column not in list_column:
        guess_column = input("Please enter a valid column, a letter from A to I ")
        
    for i, col in enumerate(list_column):
        if col == guess_column:
            guess_column_idx = i
            break
    return guess_row - 1, guess_column_idx 


def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


turns = 10
while turns > 0:
    print('Welcome to Battleship')
    print_board(player_guess_board)
    row,column = player_guess_ship_location()
    if player_guess_board[row][column] == '~':
        print(' You already guessed that ')
    elif computer_board[row][column] =='X':
        print(' Congratulations you have hit the battleship ')
        player_guess_board[row][column] = '*'
        turns -= 1
    else:
        print('Sorry, you missed')
        player_guess_board[row][column] = '~'
        turns -= 1
    if  count_hit_ships(player_guess_board) == 5:
        print("Congratulations you have sunk all the battleships ")
        break
    print(f'You have {turns} remaining ')
    if turns == 0:
        print('Game Over ')
        break