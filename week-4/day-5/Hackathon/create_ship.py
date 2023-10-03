import random


list_direction = ['H', 'V']

class Ships:
    
    def __init__(self, ship_name, range_ship: int, letter):
        self.ship_name = ship_name
        self.range_ship = range_ship
        self.letter = letter

    def create_player_ship(self, board):
        list_position_player = []
        list_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        list_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        placed_successfully = False  
        
        while not placed_successfully:  
            print(f'Choose a place for your {self.ship_name} this ship takes {self.range_ship} boxes')
            
            ply_shp_dir = input(f"In which direction do you want your {self.ship_name} to be? For vertical enter 'V', for horizontal enter 'H': ").upper()
            while ply_shp_dir not in list_direction:
                ply_shp_dir = input("Please enter a valid letter. For vertical enter 'V', for horizontal enter 'H': ").upper()
                
            print('Enter the place where you want your ship to start. If you choose "V" it will start from the top, and "H" will start from the right ')
            try:
                ply_shp_r = int(input('Enter the row here (1-9): '))
                while ply_shp_r not in list_row:
                    ply_shp_r = int(input("You have to choose a number between 1-9 "))
            except ValueError:
                ply_shp_r = int(input("You have to choose a number between 1-9 "))
                
            ply_shp_c = input('Enter the column here (A-I): ').upper()
            while ply_shp_c not in list_column:
                ply_shp_c = input("You have to choose a letter from A-I ").upper()
                
            for i, col in enumerate(list_column):
                if col == ply_shp_c:
                    ply_shp_c_idx = i
                    break
            ply_shp_r -= 1
            
            try:        
                if ply_shp_dir == 'V':
                    if all(board[ply_shp_r + i][ply_shp_c_idx] == '_' for i in range(self.range_ship)):
                        for i in range(self.range_ship):
                            board[ply_shp_r + i][ply_shp_c_idx] = self.letter
                            list_position_player.append((ply_shp_r + i, ply_shp_c_idx))
                        placed_successfully = True  
                        
                    else:
                        print("That spot is already occupied. Try again.")
                        
                if ply_shp_dir == 'H':
                    if all(board[ply_shp_r][ply_shp_c_idx + i] == '_' for i in range(self.range_ship)):
                        for i in range(self.range_ship):
                            board[ply_shp_r][ply_shp_c_idx + i] = self.letter
                            list_position_player.append((ply_shp_r, ply_shp_c_idx + i))
                        placed_successfully = True 
                        
                    else:
                        print("That spot is already occupied. Try again.")
                        
            except IndexError:
                print('Your boat is out of the board')

        return list_position_player


class Computer_ships(Ships):
    
    def __init__(self, ship_name, range_ship: int, letter, index):
        super().__init__(ship_name, range_ship, letter)
        self.ship_name = ship_name
        self.range_ship = range_ship
        self.letter = letter
        self.index = index
        
    def create_computer_ships(self, board):
        list_position_com = []
        ship_dir = random.choice(list_direction)
        if ship_dir == 'V':
            while True:
                ship_r, ship_cl = random.randint(0, self.index), random.randint(0, 8)
                if all(board[ship_r + i][ship_cl] == '_' for i in range(self.range_ship)):
                    for i in range(self.range_ship):
                        board[ship_r + i][ship_cl] = self.letter
                        list_position_com.append((ship_r + i, ship_cl))
                    break
            
        elif ship_dir == 'H':
            while True:
                ship_r, ship_cl = random.randint(0, 8), random.randint(0, self.index)
                if all(board[ship_r][ship_cl + i] == "_" for i in range(self.range_ship)):
                    for i in range(self.range_ship):
                        board[ship_r][ship_cl + i] = self.letter
                        list_position_com.append((ship_r, ship_cl + i))
                    break
        return list_position_com
            
    
