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

prompt('Welcome to Calculator!')
prompt('Please enter your first number: ')

number1 = input()
print()

while is_invalid(number1):
    prompt('Please Enter A Valid Number: ')
    number1 = input()

prompt('Thank You! Please enter your second number: ')
number2 = input()
print()

while is_invalid(number2):
    prompt('Please Enter A Valid Number: ')
    number2 = input()

prompt("Please select the number of the operation you'd like to perform: \n"
"1) Add \n"
"2) Subtract \n"
"3) Divide \n"
"4) Multiply\n")
operation = input()
print()

while operation not in ['1', '2', '3', '4']:
    prompt('Please Enter A Valid Number [1, 2, 3, 4]')
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
print()