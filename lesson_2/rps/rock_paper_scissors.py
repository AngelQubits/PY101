'''This game is intended for single player vs computer. It requires python 3.10
or later'''

import random
import os

#CONSTANT Definitions:
POSSIBLE_OUTCOME = ['rock', 'paper', 'scissors', 'r', 'p', 's']
USER_ENTRY = ['','y', 'Y', 'yes', 'n', 'N', 'no', 'Yes', 'No']
COMPUTER_CHOICE = ['rock', 'paper', 'scissors']

def run_program():
    '''This function is responsible for running the core features of the 
    program'''
    player_series_total = 0
    computer_series_total = 0
    while True:
        player_choice = user_selection()
        computer_choice = computer_selection()
        prompt('Press Enter To See Who Won This Game: ')
        input()
        game_winner = game_winner_logic(player_choice, computer_choice)
        player_series_total, computer_series_total = series_counter(
            game_winner, player_series_total, computer_series_total)
        display_game_winner(game_winner, player_choice, computer_choice,
                           player_series_total, computer_series_total)
        if computer_series_total == 3:
            prompt('Game Over: Computer Wins The Series')
        elif player_series_total == 3:
            prompt('Game Over: Congratulations You Won The Series!!!')
        elif computer_series_total + player_series_total <= 5:
            continue
        go_again = play_again()
        player_series_total = 0
        computer_series_total = 0
        if go_again.startswith(('n', 'N')):
            prompt('Thank You For Playing With Us. Have a Great Day!')
            break

def prompt(message):
    '''This function improves user readability of computer generated messages'''
    print(f'==> {message}')

def user_selection():
    '''This function is responsible for helping user select their game choice'''
    print()
    prompt('Please Make Your Choice: (Rock, Paper or Scissors)\n')
    player_entered = input().lower()
    while True:
        if player_entered not in POSSIBLE_OUTCOME:
            prompt(f'"{player_entered}" is NOT a valid Entry.'
                  f'Please Try Again. Enter Rock, Paper, or Scissors')
            player_entered = input().lower()
        else:
            break
    match player_entered[0]:
        case 'r':
            player_entered = 'rock'
        case 'p':
            player_entered = 'paper'
        case 's':
            player_entered = 'scissors'
    return player_entered.capitalize()

def computer_selection():
    '''This function is responsible for computer generated game choice'''
    computer = random.choice(COMPUTER_CHOICE)
    print()
    prompt('Computer Has Made a Choice ')
    return computer.capitalize()

def game_winner_logic(player_choice, computer_choice):
    '''This function determines winner based on game rules logic'''
    if (player_choice  == 'Rock') and (computer_choice  == 'Scissors'):
        winner = 'player'
    elif (player_choice  == 'Paper') and (computer_choice ==  'Rock'):
        winner = 'player'
    elif (player_choice  == 'Scissors') and (computer_choice == 'Paper'):
        winner = 'player'
    elif player_choice == computer_choice:
        winner = 'tied'
    else:
        winner = 'computer'
    return winner

def display_game_winner(game_winner, player_choice, computer_choice,
                       player_series_total, computer_series_total):
    '''This function prints the individual game results to the terminal'''
    print()
    print('*******************************************************************')
    print(f'You chose: {player_choice}')
    print(f'Computer Chose: {computer_choice}\n')
    if player_choice == computer_choice:
        print("It's a Tie\n")
    else:
        prompt(f"{game_winner.capitalize()} Won This Game! \n")
    print ('Current Series: \n'
           f'Player -->   {player_series_total} \n'
           f'Computer --> {computer_series_total}')
    print('*******************************************************************\n')

def series_counter(game_winner, player_series_total, computer_series_total):
    '''This function tracks the score for the series'''
    if game_winner == 'player':
        player_series_total += 1
    elif game_winner == 'computer':
        computer_series_total += 1
    elif game_winner == 'tied':
        player_series_total += 0
        computer_series_total += 0
    return player_series_total, computer_series_total
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
    if valid_go_again.startswith(('','y','Y')):
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
      "If both players choose the same item, neither player wins. It's a tie.\n"
      "You Must Win Three Out of Five Games To Win The Series.")
print('******************************************************************* \n')
prompt('Do You Want To Play? ')
prompt('(Press Enter to Continue or No to Exit)')
play = input().lower()
while True:
    if play not in USER_ENTRY:
        prompt('Press Enter to Continue or No to Exit')
        play = input().lower()
    elif play in USER_ENTRY:
        break
if play.startswith('n'):
    prompt('See You Next Time!')
#elif play in USER_ENTRY and len(play) >= 0:
else:
    prompt('Great Lets Play!!!')
    run_program()
