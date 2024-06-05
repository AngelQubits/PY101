'''Calculator program for car loan purchases above $500. Supports zero-interest
loans and positive interest loans'''

import os

def get_monthly_payment():
    '''monthly_payment function used to derive the monthly payment calculation &
print result to terminal in user friendly format'''
    if m_rate == 0:
        monthly_payment = round(loan_amount / m_duration, 2)
    else:
        monthly_payment = round(loan_amount * (m_rate /
        (1 - (1 + m_rate) ** (-m_duration))), 2)
    f_monthly_payment = '{:,}'.format(monthly_payment)
    res = round(monthly_payment * m_duration, 2)
    output = '{:,}'.format(res)
    print()
    print("*********************\nYour Monthly Payment Will Be: $",
    f_monthly_payment)
    print("You'll have a total of ", m_duration, "payments.")
    print("You will have paid a total amount of $" + output +
          " over the life of the loan.\n*********************")


def get_loan_amount():
    '''loan amount function used to get user loan amount data and validate
so it is within program limits (i.e. car loans greater than $499)'''

    print("Please Enter Your Loan Amount: ")
    while True:
        try:
            loan_amt = float(input())
            if loan_amt <= 499:
                print("Invalid Entry. Please enter value greater than $500 "
                + "(Only Numbers): ")
            else:
                values.append(loan_amt)
                break
        except ValueError:
            print("Please Enter a Valid Number Greater Than $500: ")


def get_monthly_rate():
    '''monthly rate function used to get user interest rate data and validate
so it is within program limits for rates equal to or greater than zero'''

    print()
    print("Thank You! Please Enter Your Interest Rate: " +
        "(i.e. 4.45 for 4.45% or Enter 0 for No Interest Loan): ")
    while True:
        try:
            monthly_rate = (float(input()) / 100) / 12
            if monthly_rate < 0:
                print("Invalid Entry. Please Enter 0 for No Interest Loan, or "
                + "(i.e. 4.45 for 4.45%): ")
            else:
                values.append(monthly_rate)
                break
        except ValueError:
            print("Invalid Entry. Please Enter Value Greater Than 0 " +
                "(i.e. 4.45 for 4.45%): ")


def get_monthly_duration():
    '''Loan duration function used to derive length of loan term within program 
limits of 1 year thru 7 year loans'''
    print()
    print("Now Enter Loan Term in Years (1-7): \n")
    while True:
        try:
            monthly_duration = int(input()) * 12
            if monthly_duration not in [12, 24, 36, 48, 60, 72, 84]:
                print("Invalid Entry. Please Enter a Valid Number From 1-7: ")
            else:
                values.append(monthly_duration)
                break
        except ValueError:
            print("Invalid Entry. Please Enter a Valid Number From 1-7: ")


def core():
    '''core program function used to extract code into simple 
    helper functions'''
    get_loan_amount()
    get_monthly_rate()
    get_monthly_duration()

def play_again():
    '''This function contains the repeat functionality for the program. 
    includes data validation for correct entry.'''
    while True:
        print("Would You like to continue calculating?")
        response = input()
        if response.lower() in ['yes', 'y']:
            #import os
            os.system('clear')
            break
        if response.lower() in ['no', 'n']:
            print("Thank You For Playing. 'Til Next Time. Good Bye")
            global go_again
            go_again = False
            break
        print("**Invalid Entry. Please Enter Yes or No**")
    return go_again


# Main Program Code:
print("Welcome to Our Car Loan Calculator!")

go_again = True # Main Loop value for repetitive calculations

while go_again is True:
    values = [] #list containing variables used in calculations
    core()
    loan_amount, m_rate, m_duration = values
    get_monthly_payment()
    play_again()
