from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    row1 = ' ' + ' | ' + ' ' + ' | ' + ' ' 
    row2 = '-----------' 
    print(row1.center(30,' '))
    print((board[1] + ' | ' + board[2] + ' | ' + board[3]).center(30,' '))
    print(row1.center(30,' '))
    print(row2.center(30,' '))
    print(row1.center(30,' '))
    print((board[4] + ' | ' + board[5] + ' | ' + board[6]).center(30,' '))
    print(row1.center(30,' '))
    print(row2.center(30,' '))
    print(row1.center(30,' '))
    print((board[7] + ' | ' + board[8] + ' | ' + board[9]).center(30,' '))
    print(row1.center(30,' '))

def choose_position():
    position = 'wrong'
    expected_list = ['1','2','3','4','5','6','7','8','9']
    
    while position not in expected_list:
        position = input('Choose your next position (1-9): ')

    return int(position)

def update_board(board, marker, position):
    board[position] = marker

def choose_first():
    player_number = random.randint(1,2)
    print(f'Player {player_number} will start first.\n')
    return player_number

def choose_marker():
    marker = ''
    
    while marker not in ['X','O']:
        marker = input('Player 1: Do you want to be X or O? ').upper()

        if marker not in ['X','O']:
            print('Sorry, wrong input!\n')
            continue

    return marker

def start_game_choice():
    game_on = ''
    
    while game_on.lower() not in ['yes','no']:
        game_on = input('Are you ready to play! Yes or No: ')

        if game_on.lower() not in ['yes','no']:
            print('Sorry, wrong input!\n')
            continue

    return game_on

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board

def win_check(board, marker):
    winning_sets = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    win = False
    
    for win_set in winning_sets:
        counter = 0
        for position in win_set:
            if board[position] == marker:
                counter += 1

            if counter == 3:
                return True

    return False
    
def replay_game():
    replay_choice = ''
    
    while replay_choice.lower() not in ['yes','no']:
        replay_choice = input('Do you want to play again? Yes or No: ')

        if replay_choice.lower() not in ['yes','no']:
            print('Sorry, wrong input!\n')
            continue

    if replay_choice.lower() == 'yes':
        return True
    else:
        return False

#Main Program
replay = True

while replay:
    #Initializaton
    test_board = ['Y',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    #Start 
    print('\nWelcome to Tic Tac Toe!\n')
    player1_marker = choose_marker()
    
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
     
    player = choose_first()
    
    start_game = start_game_choice()
    
    if start_game.lower() == 'yes':
        #Display board
        display_board(test_board)
    
        while True:
            #Take player1 input Input
            board_position = choose_position()
        
            if space_check(test_board, board_position):
                if player == 1:
                    #update board
                    update_board(test_board, player1_marker, board_position)
                    win = win_check(test_board, player1_marker)
                    player = 2
                else:
                    #update board
                    update_board(test_board, player2_marker, board_position)
                    win = win_check(test_board, player2_marker)
                    player = 1
            else:
                print('Choose another position. This position is not empty.\n')
                continue
                
            #Display board
            display_board(test_board)
    
            if win:
                print('Congratulations!! You have won the game.\n')
                break
                
            if full_board_check(test_board):
                print('Board is full, Nobody wins!!\n')
                break
  
        replay = replay_game()
    else:
        break
