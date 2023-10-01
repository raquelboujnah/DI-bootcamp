import random

list_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
list_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_direction = ['H', 'V']

class Ships:
    
    def __init__(self, ship_name):
        self.ship_name = ship_name


    def create_player_ship_4(self, board):
        print(f'choose a place for your {self.ship_name} this ship take 4 boxes')
        
        ply_car_dir = input(f"In witch direction you want your {self.ship_name} to be? For vertical enter 'V', for horizontal enter 'H': ").upper()
        if ply_car_dir not in list_direction:
            ply_car_dir = input("Please enter valid letter. For vertical enter 'V', for horizontal enter 'H': ").upper()
            
        print('Enter the place where you want your ship to start. If you choose "V" it will start from the top, and "H" will start from the right ')
        try:
            ply_car_r = int(input('enter the row here (1-9): '))
            while ply_car_r not in list_row:
                ply_car_r = int(input("You have to choose a number between 1-9 "))
        except ValueError:
            ply_car_r = int(input("You have to choose a number between 1-9 "))
            
        ply_car_c = input('enter the column here (A-I): ').upper()
        while ply_car_c not in list_column:
            ply_car_c = input("You have to choose a letter from A-I ").upper()
            
        for i, col in enumerate(list_column):
                if col == ply_car_c:
                    ply_car_c_idx = i
                    break
                
        if ply_car_dir == 'V':
            while board[ply_car_r - 1][ply_car_c_idx] != '_' or board[ply_car_r][ply_car_c_idx] != '_' or board[ply_car_r + 1][ply_car_c_idx] != '_' or board[ply_car_r + 2][ply_car_c_idx] != '_':
                print('one or several of those places are taken')
            board[ply_car_r - 1][ply_car_c_idx] = 'X'
            board[ply_car_r][ply_car_c_idx] = 'X'
            board[ply_car_r + 1][ply_car_c_idx] = 'X'
            board[ply_car_r + 2][ply_car_c_idx] = 'X'
            
        elif ply_car_dir == 'H':
            ply_car_r -= 1
            while board[ply_car_r][ply_car_c_idx] != '_' or board[ply_car_r][ply_car_c_idx + 1] != '_' or board[ply_car_r][ply_car_c_idx + 2] != '_' or board[ply_car_r][ply_car_c_idx + 3] != '_':
                print('one or several of those places are taken')
            board[ply_car_r][ply_car_c_idx] = 'X'
            board[ply_car_r][ply_car_c_idx + 1] = 'X'
            board[ply_car_r][ply_car_c_idx + 2] = 'X'
            board[ply_car_r][ply_car_c_idx + 3] = 'X'
        
        
    def create_player_ship_3(self, board):
        print(f'choose a place for your {self.ship_name}  this ship take 3 boxes')
        
        ply_shp_dir = input(f"In witch direction you want your {self.ship_name}  to be? For vertical enter 'V', for horizontal enter 'H': ").upper()
        if ply_shp_dir not in list_direction:
            ply_shp_dir = input("Please enter valid letter. For vertical enter 'V', for horizontal enter 'H': ").upper()
            
        print(f'Enter the place where you want your {self.ship_name} to start. If you choose "V" it will start from the top, and "H" will start from the right ')
        try:
            ply_shp_r = int(input('enter the row here (1-9): '))
            while ply_shp_r not in list_row:
                ply_shp_r = int(input("You have to choose a number between 1-9 "))
        except ValueError:
            ply_shp_r = int(input("You have to choose a number between 1-9 "))
            
        ply_shp_c = input('enter the column here (A-I): ').upper()
        while ply_shp_c not in list_column:
            plyshpt_c = input("You have to choose a letter from A-I ").upper()
            
        for i, col in enumerate(list_column):
                if col == ply_shp_c:
                    ply_shp_c_idx = i
                    break
                
        if ply_shp_dir == 'V':
            while board[ply_shp_r - 1][ply_shp_c_idx] != '_' or board[ply_shp_r][ply_shp_c_idx] != '_' or board[ply_shp_r + 1][ply_shp_c_idx] != '_':
                print('one or several of those places are taken')
            board[ply_shp_r - 1][ply_shp_c_idx] = 'D'
            board[ply_shp_r][ply_shp_c_idx] = 'D'
            board[ply_shp_r + 1][ply_shp_c_idx] = 'D'
            
        elif ply_shp_dir == 'H':
            ply_shp_r -= 1
            while board[ply_shp_r][ply_shp_c_idx] != '_' or board[ply_shp_r][ply_shp_c_idx + 1] != '_' or board[ply_shp_r][ply_shp_c_idx + 2] != '_':
                print('one or several of those places are taken')
            board[ply_shp_r][ply_shp_c_idx] = 'D'
            board[ply_shp_r][ply_shp_c_idx + 1] = 'D'
            board[ply_shp_r][ply_shp_c_idx + 2] = 'D'
            
            
    def create_player_ship_2(self, board):
        print(f'Choose a place for your {self.ship_name}  this ship take 2 boxes')
        
        ply_shp_dir = input(f"In witch direction you want your {self.ship_name}  to be? For vertical enter 'V', for horizontal enter 'H': ").upper()
        if ply_shp_dir not in list_direction:
            ply_shp_dir = input("Please enter valid letter. For vertical enter 'V', for horizontal enter 'H': ").upper()
            
        print(f'Enter the place where you want your {self.ship_name} to start. If you choose "V" it will start from the top, and "H" will start from the right ')
        try:
            ply_shp_r = int(input('Enter the row here (1-9): '))
            while ply_shp_r not in list_row:
                ply_shp_r = int(input("You have to choose a number between 1-9 "))
        except ValueError:
            ply_shp_r = int(input("You have to choose a number between 1-9 "))
            
        ply_shp_c = input('Enter the column here (A-I): ').upper()
        while ply_shp_c not in list_column:
            plyshpt_c = input("You have to choose a letter from A-I ").upper()
            
        for i, col in enumerate(list_column):
                if col == ply_shp_c:
                    ply_shp_c_idx = i
                    break
                
        if ply_shp_dir == 'V':
            while board[ply_shp_r - 1][ply_shp_c_idx] != '_' or board[ply_shp_r][ply_shp_c_idx] != '_':
                print('one or several of those places are taken')
            board[ply_shp_r - 1][ply_shp_c_idx] = 'O'
            board[ply_shp_r][ply_shp_c_idx] = 'O'
                        
        elif ply_shp_dir == 'H':
            ply_shp_r -= 1
            while board[ply_shp_r][ply_shp_c_idx] != '_' or board[ply_shp_r][ply_shp_c_idx + 1] != '_':
                print('one or several of those places are taken')
            board[ply_shp_r][ply_shp_c_idx] = 'O'
            board[ply_shp_r][ply_shp_c_idx + 1] = 'O'
            

class Computer_ships(Ships):
    
    def __init__(self, ship_name):
        super().__init__(ship_name)
        self.ship_name = ship_name
        
    def create_computer_ships_4(self, board):
        ship_dir = random.choice(list_direction)
        ship_r, ship_cl = random.randint(0, 9), random.randint(0, 9)
        if ship_dir == 'V':
            while board[ship_r][ship_cl] == 'X' or board[ship_r + 1][ship_cl] == 'X' or board[ship_r + 2][ship_cl] == 'X' or board[ship_r + 3][ship_cl] == 'X':
                ship_r, ship_cl = random.randint(0, 9), random.randint(0, 9)
            board[ship_r][ship_cl] = 'X'
            board[ship_r + 1][ship_cl] = 'X'
            board[ship_r + 2][ship_cl] = 'X'
            board[ship_r + 3][ship_cl] = 'X'
            
        if ship_dir == 'H':
            while board[ship_r][ship_cl] == 'X' or  board[ship_r][ship_cl + 1] == 'X' or board[ship_r][ship_cl + 2] == 'X' or board[ship_r][ship_cl + 3] == 'X':
                ship_r, ship_cl = random.randint(0, 9), random.randint(0, 9)
            board[ship_r][ship_cl] = 'X'
            board[ship_r][ship_cl + 1] = 'X'
            board[ship_r][ship_cl + 2] = 'X'
            board[ship_r][ship_cl + 3] = 'X'
            
            
    def create_computer_ships_3(self, board):
        ship_dir = random.choice(list_direction)
        ship_r, ship_cl = random.randint(0, 9), random.randint(0, 9)
        if ship_dir == 'V':
            while board[ship_r][ship_cl] == 'X' or board[ship_r + 1][ship_cl] == 'X' or board[ship_r + 2][ship_cl] == 'X':
                ship_r, ship_cl = random.randint(0, 9), random.randint(0, 9)
            board[ship_r][ship_cl] = 'X'
            board[ship_r + 1][ship_cl] = 'X'
            board[ship_r + 2][ship_cl] = 'X'
            
        if ship_dir == 'H':
            while board[ship_r][ship_cl] == 'X' or  board[ship_r][ship_cl + 1] == 'X' or board[ship_r][ship_cl + 2] == 'X':
                ship_r, ship_cl = random.randint(0, 9), random.randint(0, 9)
            board[ship_r][ship_cl] = 'X'
            board[ship_r][ship_cl + 1] = 'X'
            board[ship_r][ship_cl + 2] = 'X'
            
    def create_computer_ships_2(self, board):
        ship_dir = random.choice(list_direction)
        ship_r, ship_cl = random.randint(0, 9), random.randint(0, 9)
        if ship_dir == 'V':
            while board[ship_r][ship_cl] == 'X' or board[ship_r + 1][ship_cl] == 'X':
                ship_r, ship_cl = random.randint(0, 9), random.randint(0, 9)
            board[ship_r][ship_cl] = 'X'
            board[ship_r + 1][ship_cl] = 'X'
            
        if ship_dir == 'H':
            while board[ship_r][ship_cl] == 'X' or  board[ship_r][ship_cl + 1] == 'X':
                ship_r, ship_cl = random.randint(0, 9), random.randint(0, 9)
            board[ship_r][ship_cl] = 'X'
            board[ship_r][ship_cl + 1] = 'X'

