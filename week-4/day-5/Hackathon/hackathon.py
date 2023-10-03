import random
import json
from create_ship import Ships
from create_ship import Computer_ships
from check_hit_win import player_turn
from check_hit_win import computer_turn
from check_hit_win import check_hit
from check_hit_win import chek_if_sank
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
com_guess_board = [['_']*9 for x in range(9)]


let_to_num = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7} #--------------------------------------
list_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
list_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]


#print board for the right player
def print_board(board):
    print('  A B C D E F G H I')
    row_num = 1
    for row in board:
        print(row_num, "|".join(row))
        row_num += 1










# turns = 10
# while turns > 0:
#     print('Welcome to Battleship')
#     print_board(player_guess_board)
#     row,column = player_guess_ship_location()
#     if player_guess_board[row][column] == '~':
#         print(' You already guessed that ')
#     elif computer_board[row][column] =='X':
#         print(' Congratulations you have hit the battleship ')
#         player_guess_board[row][column] = '*'
#         turns -= 1
#     else:
#         print('Sorry, you missed')
#         player_guess_board[row][column] = '~'
#         turns -= 1
#     if  count_hit_ships(player_guess_board) == 5:
#         print("Congratulations you have sunk all the battleships ")
#         break
#     print(f'You have {turns} remaining ')
#     if turns == 0:
#         print('Game Over ')
#         break
    
#to get the names of the players
def get_names():
    player_name = input("Enter your name: ")
    with open('names.json', "r") as jsfile:
            names_json = json.load(jsfile)
    computer_name = random.choice(names_json)
    return player_name, computer_name



ship1_ply = Ships("Carrier", 4, 'X')
ship2_ply = Ships('Battleship', 4, 'K')
ship3_ply = Ships('Cruiser', 3, 'D')
ship4_ply = Ships('Submarine', 2, 'O')
ship5_ply = Ships('Destroyer', 2, 'H')

# print_board(player_board)
# ship1_ply.create_player_ship(player_board)
# print_board(player_board)
# ship2_ply.create_player_ship(player_board)
# print_board(player_board)
# ship3_ply.create_player_ship(player_board)
# print_board(player_board)
# ship4_ply.create_player_ship(player_board)
# print_board(player_board)
# ship5_ply.create_player_ship(player_board)
# print_board(player_board)

ship1_com = Computer_ships("Carrier", 4, 'X', 5)
ship2_com = Computer_ships('Battleship', 4, 'K', 5)
ship3_com = Computer_ships('Cruiser', 3, 'D', 6)
ship4_com = Computer_ships('Submarine', 2, 'O', 7)
ship5_com = Computer_ships('Destroyer', 2, 'H', 7)

ship6_com = Computer_ships("Carrier", 4, 'X', 5)
ship7_com = Computer_ships('Battleship', 4, 'K', 5)
ship8_com = Computer_ships('Cruiser', 3, 'D', 6)
ship9_com = Computer_ships('Submarine', 2, 'O', 7)
ship10_com = Computer_ships('Destroyer', 2, 'H', 7)

ship6_com.create_computer_ships(player_board)
ship7_com.create_computer_ships(player_board)
ship8_com.create_computer_ships(player_board)
ship9_com.create_computer_ships(player_board)
ship10_com.create_computer_ships(player_board)
print_board(player_board)

ship1_com.create_computer_ships(computer_board)
ship2_com.create_computer_ships(computer_board)
ship3_com.create_computer_ships(computer_board)
ship4_com.create_computer_ships(computer_board)
ship5_com.create_computer_ships(computer_board)
print_board(computer_board)

ply_list_X = []
ply_list_K = []
ply_list_D = []
ply_list_O = []
ply_list_H = []

com_list_X = []
com_list_K = []
com_list_D = []
com_list_O = []
com_list_H = []     
 

count = 0
while count < 8:
    print_board(player_guess_board)
    pos = player_turn(player_guess_board)
    g_guesses = check_hit(player_guess_board, computer_board, pos)
    print_board(player_guess_board)
    chek_if_sank(computer_board, g_guesses, ply_list_X, ply_list_K, ply_list_D, ply_list_O, ply_list_H)
    
    com_pos = computer_turn(com_guess_board)
    com_g_guesses = check_hit(com_guess_board, player_board, com_pos)
    print_board(com_guess_board)
    chek_if_sank(player_board, com_g_guesses, com_list_X, com_list_K, com_list_D, com_list_O, com_list_H)
    count += 1





