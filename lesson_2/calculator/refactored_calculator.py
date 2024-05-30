'''
This refactored calculator is using match case statement.
Thus it requires python 3.10.xx or newer.
'''

def prompt(message):
    '''This function is meant to add an arrow to all
	   program generated messages'''
    print(f'=> {message}')

def is_invalid(number_str):
    '''This function is meant to check the validity of user input, 
    bypass ValueError and prompt user to re-enter a valid input'''
    try:
        int(number_str)
    except ValueError:
        return True
    return False

def calc_core():
   '''This function is the core program of the calculator and can be run
   again by invoking it'''

   prompt(data["message1"])
   number1 = input()
   print()
   while is_invalid(number1):
       prompt(data["message2"])
       number1 = input()
   
   prompt(data["message3"])
   number2 = input()
   print()
   
   while is_invalid(number2):
       prompt(data["message2"])
       number2 = input()
   
   prompt(data["message4"])
   operation = input()
   print()
   
   while operation not in ['1', '2', '3', '4']:
        prompt(data["message5"])
        operation = input()
   match operation:
       case '1':
           output = int(number1) + int(number2)
       case '2':
           output = int(number1) - int(number2)
       case '3':
           output = int(number1) / int(number2)
       case '4':
           output = int(number1) * int(number2)
   prompt(f'Your result is: {output} \n')

import json
with open('calculator_messages.json', 'r') as file:
    data = json.load(file)
 
prompt(data["welcome"])
calc_core()

while True:
 prompt(data["message7"])
 again = input()
 if again == '2':
  prompt(data["message8"])
  break
 if again == '1':
  calc_core()
  continue
 else:
  prompt(data["message9"])
  again = input()
