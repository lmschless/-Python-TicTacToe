## Author: Luke Schlessinger, 10/31/19
## Source: Automate The Boring Stuff by Al Sweigart
## Edits: 10/31/19: Resolved bug where turns were not alternating between players correctly.
##                  edited the if statements indents for Player 2 logic.

#import os for clear function, import range for choose_first function
import os
import random

def display_board(board):
    os.system('CLS')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    
######
    
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
######
    
def place_marker(board, marker, position):
    
    board[position] = marker
    
######
    
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

######

def choose_first():
    choices = ['Player 1','Player 2']
    return random.choice(choices)

######

def space_check(board, position):
    
    return board[position] == ' '

######

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

######

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

######

def replay():
    playAgain = input('Play again? Enter: Yes or No ')
    return playAgain.lower() == 'yes'

######

print('Welcome to Tic Tac Toe!')

while True: 
    ## Game set up, the board, markers, who goes first
    
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first') 
    
    play_game = input('Ready to play? y or n ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    

    while game_on:
#Player 1 Turn 
        if turn == 'Player 1':
    #Show the board
            display_board(the_board)
    #Choose a position
            position = player_choice(the_board)
    #Place the marker on the position they chose
            place_marker(the_board,player1_marker,position)
    #Check if they won, or check if there is a tie
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 wins!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is tied')
                    break
                else:
                    turn = 'Player 2'
        
#No tie and no win, then next players turn
    
 # Player2's turn.       
        else:
            display_board(the_board)
    #Choose a position
            position = player_choice(the_board)
    #Place the marker on the position they chose
            place_marker(the_board,player2_marker,position)
    #Check if they won, or check if there is a tie
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 wins!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tied game')
                    break
                else:
                    turn = 'Player 1'            
            

    if not replay():
        break



