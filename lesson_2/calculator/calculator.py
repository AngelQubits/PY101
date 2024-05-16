# Welcome the user to your calculator program
# Ask the user for the first number
# Ask the user for the second number
# Ask the user for the operation to perform
# Perform the opertion on the two Numbers
# Print the result to the terminal

print('Welcome to Calculator!\n'
'Please enter your first number: ')

number1 = int(input())
print()

print('Thank You! Please enter your second number: ')
number2 = int(input())
print()

print("Please select the number of the operation you'd like to perform: \n"
"1) Add \n"
"2) Subtract \n"
"3) Divide \n"
"4) Multiply\n")
operation = input()
print()

if operation == '1':
	output = number1 + number2
elif operation == '2':
	output = number1 - number2
elif operation == '3':
	output = number1 / number2
elif operation == '4':
	output = number1 * number2
	
print(f'Your result is: {output} \n')