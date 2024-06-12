'''This game is intended for single player vs computer'''

import random
import os

#CONSTANT Definitions:
POSSIBLE_OUTCOME = ['rock', 'paper', 'scissors']
USER_ENTRY = ['','y', 'Y', 'yes', 'n', 'N', 'no', 'Yes', 'No']

def run_program():
    '''This function is responsible for running the core features of the 
    program'''
    while True:
        player_choice = user_selection()
        computer_choice = computer_selection()
        prompt('Press Enter To See Who Won: ')
        input()
        game_winner = game_winner_logic(player_choice, computer_choice)
        display_winner(game_winner, player_choice, computer_choice)
        go_again = play_again()
        if go_again.startswith(('n', 'N')):
            prompt('Thank You For Playing With Us. Have a Great Day!')
            break

def prompt(message):
    '''This function improves user readability of computer generated messages'''
    print(f'==> {message}')

def user_selection():
    '''This function is responsible for helping user select their game choice'''
    print()
    prompt('Great Lets Play!!!')
    prompt('Please Make Your Choice: (Rock, Paper or Scissors)\n')
    player_entered = input().lower()
    while True:
        if player_entered not in POSSIBLE_OUTCOME:
            prompt(f'{player_entered} is NOT a valid Entry.'
                  f'Please Try Again. Enter Rock, Paper, or Scissors')
            player_entered = input().lower()
        else:
            break
    return player_entered.capitalize()

def computer_selection():
    '''This function is responsible for computer generated game choice'''
    computer = random.choice(POSSIBLE_OUTCOME)
    print()
    prompt('Computer Has Made a Choice ')
    return computer.capitalize()

def game_winner_logic(player_choice, computer_choice):
    '''This function determines winner based on game rules logic'''
    if (player_choice  == 'Rock') and (computer_choice  == 'Scissors'):
        winner = player_choice
    elif (player_choice  == 'Paper') and (computer_choice ==  'Rock'):
        winner = player_choice
    elif (player_choice  == 'Scissors') and (computer_choice == 'Paper'):
        winner = player_choice
    else:
        winner = computer_choice
    return winner

def display_winner(game_winner, player_choice, computer_choice):
    '''This function prints the final game results to the terminal'''
    print()
    print('*******************************************************************')
    print(f'You chose: {player_choice}')
    print(f'Computer Chose: {computer_choice}')
    print(f'The Winner is: {game_winner}')
    if player_choice == computer_choice:
        print("It's a Tie")
    elif game_winner == player_choice:
        prompt('Congratulations, YOU WIN!!!')
    elif game_winner == computer_choice:
        prompt("I'm sorry, better luck next time")
    print('*******************************************************************\n')

def play_again():
    '''This function offers the user the ability to continue playing'''
    prompt('Would You like to Play Again? ')
    user_goes_again = input().capitalize()
    def play_again_valid(go_again):
        '''This function determines the validity of play again entry.  Pylint
        was raising an error stating either or all none statements in function 
        should return an expression or none of them.  Nesting the function
        solved this'''
        while True:
            if go_again not in USER_ENTRY:
                prompt(f' {go_again} is NOT a valid entry')
                print('Please Enter A Valid Entry: (i.e. Yes or No)')
                go_again = input().capitalize()
            else:
                return go_again
    valid_go_again = play_again_valid(user_goes_again)
    if valid_go_again.startswith(('n', 'N')):
        os.system('clear')
        return valid_go_again
    if valid_go_again.startswith(('y','Y')):
        prompt("Let's Go Again!")
        os.system('clear')
        return valid_go_again

# Welcome To The Program:
prompt('Welcome To RPS!!!')
prompt('The Rules of The Game Are As Follows: \n')
print('*******************************************************************')
print('If You choose rock and the Computer chooses scissors, You win. \n'
      'If You choose paper and the Computer chooses rock, You win! \n'
      'If You choose scissor and the Computer chooses paper, You win! \n'
      "If both players choose the same item, neither player wins. It's a tie.")
print('******************************************************************* \n')
prompt('Do You Want To Play? ')
prompt('(Press Enter to Continue or No to Exit)')
play = input().lower()
if play == 'no':
    prompt('See You Next Time!')
elif play in USER_ENTRY and len(play) >= 0:
    run_program()
