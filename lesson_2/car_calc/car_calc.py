print("Welcome to Our Car Loan Calculator!")
print("Please Enter Your Loan Amount: ")
while True:
    try:
	    loan_amt = float(input())
	    if loan_amt <= 499:
		    print("Invalid Entry. Please enter value greater than $500 "
		    + "(Only Numbers): ")
	    else:
		    break
    except ValueError:
        print("Please Enter a Valid Number Greater Than $500: ")

print()
print("Thank You! Please Enter Your Interest Rate: ")
while True:
	try:
		monthly_rate = (float(input()) / 100) / 12
		if monthly_rate < 0:
			print("Invalid Entry. Please Enter Value Greater Than 0 " +
			    "(i.e. 4.45 for 4.45%): ")
		else:
		    break
	except ValueError:
		print("Invalid Entry. Please Enter Value Greater Than 0 " +
			    "(i.e. 4.45 for 4.45%): ")
	    

print()
print("Now Enter Loan Term in Years (1-7): \n")
while True:
	try:
		monthly_duration = int(input()) * 12
		if monthly_duration not in [12, 24, 36, 48, 60, 72, 84]:
			print("Invalid Entry. Please Enter a Valid Number From 1-7: ")
		else:
			break
	except ValueError:
		print("Invalid Entry. Please Enter a Valid Number From 1-7: ")
		

def monthly_payment():
	mp = round(loan_amt * (monthly_rate / (1 - (1 + monthly_rate) ** (-monthly_duration))), 2)
	monthly_payment = '{:,}'.format(mp)
	res = round(mp * monthly_duration, 2)
	output = '{:,}'.format(res)
	print()
	print("*********************\nYour Monthly Payment Will Be: $", monthly_payment)
	print("You'll have a total of ", monthly_duration, "payments.")
	print("You will have paid a total amount of $" + output + 
	      " over the life of the loan.\n*********************")

monthly_payment()