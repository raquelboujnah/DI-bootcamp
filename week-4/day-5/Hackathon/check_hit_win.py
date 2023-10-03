import random
list_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
list_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def player_turn(board):
    guess_empty = False
    while guess_empty == False:
        print('Try to guess where your adversair places his boats')
        try:
            ply_guess_r = int(input('Enter the row: '))
            while ply_guess_r not in list_row:
                ply_guess_r = int(input('You have to enter a number from 1 to 9 '))
        except ValueError:
            ply_guess_r = int(input('You have to enter a number from 1 to 9 '))
            
        ply_guess_c = input('Enter the column: ').upper()
        while ply_guess_c not in list_column:
            ply_guess_c = input('You have to enter a letter from A to I ')
            
        
        for i, col in enumerate(list_column):
            if col == ply_guess_c:
                ply_guess_c_idx = i
                break
        ply_guess_r -= 1
        
        if board[ply_guess_r][ply_guess_c_idx] == '_':
            board[ply_guess_r][ply_guess_c_idx] = '-'
            guess_empty = True
        else:
            print('You already guessed this spot')
            
    return (ply_guess_r, ply_guess_c_idx)

def computer_turn(board):
    while True:
        com_guess_r, com_guess_c = random.randint(0, 8), random.choice(list_column)
        for i, col in enumerate(list_column):
            if col == com_guess_c:
                com_guess_c_idx = i
                break
            
        if board[com_guess_r][com_guess_c_idx] == '_':
            board[com_guess_r][com_guess_c_idx] = '-'
            print(f'the computer guess is: {com_guess_r + 1}, {com_guess_c}')
            break
    
    return (com_guess_r, com_guess_c_idx)

def check_hit(board_ply, board2, ply_pos):
    good_guesses = []
    r, c = ply_pos
    if board2[r][c] != '_':
        print('a ship was hit!')
        board_ply[r][c] = '*'
        good_guesses.append((r, c))
    else:
        print('Missed')
        
    return good_guesses


def chek_if_sank(board, g_guesses, list_X: list, list_K: list, list_D: list, list_O: list, list_H: list):
    for pos in g_guesses:
        if board[pos[0]][pos[1]] == 'X':
            list_X.append(pos)
        elif board[pos[0]][pos[1]]== 'K':
            list_K.append(pos)
        elif board[pos[0]][pos[1]] == 'D':
            list_D.append(pos)
        elif board[pos[0]][pos[1]] == 'O':
            list_O.append(pos)
        elif board[pos[0]][pos[1]] == 'H':
            list_H.append(pos)
    print(list_X)
    print(list_K)
    print(list_D)
    print(list_O)
    print(list_H)
    
    
    if len(list_X) == 4:
        print('You sank his Carrier')
        list_X.clear()
    elif len(list_K) == 4:
        print('You sank his Battleship')
        list_K.clear()
    elif len(list_D) == 3:
        print('You sank his Cruiser')
        list_D.clear()
    elif len(list_O) == 2:
        print('You sank his Submarine')
        list_O.clear()
    elif len(list_H) == 2:
        print('You sank his Destroyer')
        list_H.clear()
