'''Calculator program for car loan purchases above $500. Supports zero-interest
loans and positive interest loans'''

import os

def prompt(message):
    '''This function is used to differentiate Computer Message vs User Input'''
    print(f'===> {message}')

def calculate_monthly_payment(calculated_loan_amount, calculated_rate,
                              calculated_duration):
    '''This function used to derive the monthly payment calculation'''
    if calculated_rate == 0:
        monthly_payment = round(calculated_loan_amount / calculated_duration, 2)
    else:
        monthly_payment = round(calculated_loan_amount * (calculated_rate /
        (1 - (1 + calculated_rate) ** (-calculated_duration))), 2)
    f_monthly_payment = f'{monthly_payment:,.2f}'
    res = monthly_payment * calculated_duration
    total_paid = f'{res:,.2f}'
    return f_monthly_payment, total_paid

def display_monthly_payment(f_monthly_payment, calculated_duration, total_paid,
                            loan_response, calculated_rate, duration_output):
    '''This function used to print result to terminal in user friendly format'''
    annual_loan_rate = calculated_rate * 12 * 100
    loan_rate_output = f'{annual_loan_rate:,.2f}'
    print("************************************************************")
    print("You Entered The Following: ")
    print(f"Loan Amount: {loan_response} \n"
          f"Annual Interest Rate: {loan_rate_output}% \n"
          f"Loan Duration: {duration_output} Years")
    print(f"Your Monthly Payment Will Be: ${f_monthly_payment}")
    print("You'll have a total of", round(calculated_duration), "payments.")
    print("You will have paid a total amount of $" + total_paid +
          " over the life of the loan.\n")
    print("************************************************************")

def get_loan_amount():
    '''loan amount function used to get user loan amount data and validate
so it is within program limits (i.e. car loans greater than $499)'''

    prompt("Please Enter Your Loan Amount: " +
        "(i.e. 1234.56 for $1,234.56 or Enter 0 for No Interest Loan): ")
    while True:
        try:
            loan_amt = float(input())
            loan_response = f'{loan_amt:,.2f}'
            if loan_amt <= 499:
                prompt("Invalid Entry. Please enter value greater than $500 \n" +
                "(i.e. 1234.56 for $1,234.56 or Enter 0 for No Interest Loan): ")
            else:
                return loan_amt, loan_response
        except ValueError:
            prompt("Invalid Entry. Please enter value greater than $500 \n" +
                "(i.e. 1234.56 for $1,234.56 or Enter 0 for No Interest Loan): ")

def get_monthly_rate():
    '''monthly rate function used to get user interest rate data and validate
so it is within program limits for rates equal to or greater than zero'''

    print()
    prompt("Thank You! Please Enter Your Interest Rate: " +
        "(i.e. 4.45 for 4.45% or Enter 0 for No Interest Loan): ")
    while True:
        try:
            monthly_rate = (float(input()) / 100) / 12
            if monthly_rate < 0:
                prompt("Invalid Entry. Please Enter 0 for No Interest Loan, or "
                + "(i.e. 4.45 for 4.45%): ")
            else:
                return monthly_rate
        except ValueError:
            prompt("Invalid Entry. Please Enter Value Greater Than 0 " +
                "(i.e. 4.45 for 4.45%): ")

def get_monthly_duration():
    '''Loan duration function used to derive length of loan term within program 
limits of 1 year thru 7 year loans'''
    print()
    prompt("Now Enter Loan Term in Years (1-7): ")
    while True:
        try:
            monthly_duration = float(input()) * 12
            duration_response = monthly_duration / 12
            duration_output = f'{duration_response:,.2f}'
            if monthly_duration <= 0.00:
                prompt("Invalid Entry. Please Enter a Valid Number Greater than 0: ")
            else:
                return monthly_duration, duration_output
        except ValueError:
            prompt("Invalid Entry. Please Enter a Valid Number Greater Than 0: ")

def play_again():
    '''This function contains the repeat functionality for the program. 
    includes data validation for correct entry.'''
    while True:
        prompt("Would You like to continue calculating?")
        response = input()
        if response.lower() in ['yes', 'y']:
            os.system('clear')
            return True
        if response.lower() in ['no', 'n']:
            prompt("Thank You For Playing. 'Til Next Time. Good Bye")
            return None
        prompt("**Invalid Entry. Please Enter Yes or No**")

def run_calculator():
    '''This is the main program code'''
    prompt("Welcome to Our Car Loan Calculator!")

    go_again = True # Main Loop value for repetitive calculations

    while go_again is True:
        calculated_loan_amount, loan_response = get_loan_amount()
        calculated_rate = get_monthly_rate()
        calculated_duration, duration_output = get_monthly_duration()
        f_monthly_payment, total_paid = calculate_monthly_payment(calculated_loan_amount,
                                    calculated_rate, calculated_duration)
        display_monthly_payment(f_monthly_payment, calculated_duration, total_paid,
                                loan_response, calculated_rate, duration_output)
        go_again = play_again()

run_calculator()
