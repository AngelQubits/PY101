print("Welcome to Our Car Loan Calculator!")
print("Please Enter Your Loan Amount: ")
loan_amt = float(input())
# if loan_amt <= 0:
# 	print("Invalid Entry. Please enter value greater than 1.")

print()
print("Thank You! Please Enter Your Interest Rate: ")
monthly_rate = (float(input()) / 100) / 12
#print("$", loan_amt, "This is your monthly rate: ", monthly_rate, "%")

print()
print("Now Enter Loan Term in Years (1-7): \n")
monthly_duration = int(input()) * 12

def monthly_payment():
	mp = round(loan_amt * (monthly_rate / (1 - (1 + monthly_rate) ** (-monthly_duration))), 2)
	monthly_payment = '{:,}'.format(mp)
	res = round(mp * monthly_duration, 2)
	output = '{:,}'.format(res)
	print("*********************\nYour Monthly Payment Will Be: $", monthly_payment)
	print("You'll have a total of ", monthly_duration, "payments.")
	print("You will have paid a total amount of $" + output + 
	      " over the life of the loan.\n*********************")

monthly_payment()