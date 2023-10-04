import random
import json
from create_ship import Player_ships
from create_ship import Computer_ships
from check_hit_win import player_turn
from check_hit_win import computer_turn
from check_hit_win import check_hit
from check_hit_win import chek_if_sank

computer_board = [['_']*9 for x in range(9)]
player_guess_board = [['_']*9 for x in range(9)]
player_board = [['_']*9 for x in range(9)]
com_guess_board = [['_']*9 for x in range(9)]


let_to_num = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7, 'I':8} #--------------------------------------
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
 

#print the right board for the right player
def print_board(board):
    print('  A B C D E F G H I')
    row_num = 1
    for row in board:
        print(row_num, "|".join(row))
        row_num += 1


#to get the names of the players
def get_names():
    player_name = input("Enter your name Admiral: ").capitalize()
    with open('names.json', "r") as jsfile:
            names_json = json.load(jsfile)
    computer_name = random.choice(names_json)
    return player_name, computer_name



# ship1_ply = Player_ships("Carrier", 4, 'X')
# ship2_ply = Player_ships('Battleship', 4, 'K')
# ship3_ply = Player_ships('Cruiser', 3, 'D')
# ship4_ply = Player_ships('Submarine', 2, 'O')
# ship5_ply = Player_ships('Destroyer', 2, 'H')

# ship6_com = Computer_ships("Carrier", 4, 'X', 5)
# ship7_com = Computer_ships('Battleship', 4, 'K', 5)
# ship8_com = Computer_ships('Cruiser', 3, 'D', 6)
# ship9_com = Computer_ships('Submarine', 2, 'O', 7)
# ship10_com = Computer_ships('Destroyer', 2, 'H', 7)

# ship6_com.create_computer_ships(player_board)
# ship7_com.create_computer_ships(player_board)
# ship8_com.create_computer_ships(player_board)
# ship9_com.create_computer_ships(player_board)
# ship10_com.create_computer_ships(player_board)
# print_board(player_board)

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

# ship1_com = Computer_ships("Carrier", 4, 'X', 5)
# ship2_com = Computer_ships('Battleship', 4, 'K', 5)
# ship3_com = Computer_ships('Cruiser', 3, 'D', 6)
# ship4_com = Computer_ships('Submarine', 2, 'O', 7)
# ship5_com = Computer_ships('Destroyer', 2, 'H', 7)

# ship1_com.create_computer_ships(computer_board)
# ship2_com.create_computer_ships(computer_board)
# ship3_com.create_computer_ships(computer_board)
# ship4_com.create_computer_ships(computer_board)
# ship5_com.create_computer_ships(computer_board)
# print_board(computer_board)





def main():
    print("---------------------------\n"
      "        BATTLESHIPS\n"
      "---------------------------\n")

    print("Welcome to Battleships Admiral!\n")
    
    ply_name, com_name = get_names()
    
    print(f"Admiral {ply_name} we've spotted an enemy, a so-called {com_name}, fleet in our harbour and it's up to you to sink them!\n"
          "You'll need to hit the BATTLESHIP (alias 'K') and the CARRIER (alias 'X') 4 times to get through the thick armour.\n"
          "There are also small ships as the DESTROYER (alias 'H') or the SUBMARINE (alias 'O') that will take two hits, but be careful, it packs a punch!\n"
          "Then there is a CRUISER (alias 'D') that will need to be hit three times.\n\n"
          "Your navigator has been given a map of the seas. Place your ships in the most strategic way.\n"
          "Fire your missiles into one of the coordinates on the map.\n"
          "Pick your shots carefully, if you waste missiles you will waste also time!.\n"
          "When you will hit a ship a '*' will appears at the coordinates where the ship was hit, else, a '-' will appears"
          "It's all up to you now Admiral, GOOD LUCK!\n"
          "---------------------------\n")
    
    ship1_ply = Player_ships("Carrier", 4, 'X')
    ship2_ply = Player_ships('Battleship', 4, 'K')
    ship3_ply = Player_ships('Cruiser', 3, 'D')
    ship4_ply = Player_ships('Submarine', 2, 'O')
    ship5_ply = Player_ships('Destroyer', 2, 'H')
    
    print_board(player_board)
    ship1_ply.create_player_ship(player_board, ply_name)
    print_board(player_board)
    ship2_ply.create_player_ship(player_board, ply_name)
    print_board(player_board)
    ship3_ply.create_player_ship(player_board, ply_name)
    print_board(player_board)
    ship4_ply.create_player_ship(player_board, ply_name)
    print_board(player_board)
    ship5_ply.create_player_ship(player_board, ply_name)
    print_board(player_board)

    print('All your ships are placed. May the best win!')
    
    ship1_com = Computer_ships("Carrier", 4, 'X', 5)
    ship2_com = Computer_ships('Battleship', 4, 'K', 5)
    ship3_com = Computer_ships('Cruiser', 3, 'D', 6)
    ship4_com = Computer_ships('Submarine', 2, 'O', 7)
    ship5_com = Computer_ships('Destroyer', 2, 'H', 7)

    ship1_com.create_computer_ships(computer_board)
    ship2_com.create_computer_ships(computer_board)
    ship3_com.create_computer_ships(computer_board)
    ship4_com.create_computer_ships(computer_board)
    ship5_com.create_computer_ships(computer_board)
    
    print_board(computer_board)
    count_hit_ply = 0
    count_hit_com = 0
    print(f'Now that you are all set Admiral {ply_name}, try to guess where your ennemi places his boats. Here is your map:')
    while count_hit_ply < 5 :
        print_board(player_guess_board)
        pos = player_turn(player_guess_board, ply_name)
        g_guesses = check_hit(player_guess_board, computer_board, pos, ply_name)
        print_board(player_guess_board)
        count_ply = chek_if_sank(computer_board, g_guesses, ply_name, ply_list_X, ply_list_K, ply_list_D, ply_list_O, ply_list_H)
        count_hit_ply += count_ply
        print(f'You have sank already {count_hit_ply} ships')
        
        com_pos = computer_turn(com_guess_board, com_name)
        com_g_guesses = check_hit(com_guess_board, player_board, com_pos, com_name)
        print_board(com_guess_board)
        count_com = chek_if_sank(player_board, com_g_guesses, com_name, com_list_X, com_list_K, com_list_D, com_list_O, com_list_H)
        count_hit_com += count_com
        print(f'{com_name} has sank already {count_hit_ply} ships')


main()

