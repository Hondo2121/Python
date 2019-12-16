a = float(input("enter a number: "))
b = float(input("enter a second number: "))

if (a != b):
	if (a > b and a >= 0 and b >= 0):
		print("Your first number is greater than your second number")
	elif (a < b and a >=0 and b >= 0):
		print("Your first number is less than your second number")

elif (a < 0 or b < 0):
	print("error")

elif (a == b and a >= 0 and b >= 0):
	print("Your numbers are equal and are both positive")
	
