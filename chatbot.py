n = input("What is your name?")
print()

print("Hi there " + n + ", nice to meet you.")
age = int(input("How old are you? "))
print()

print(str(age) + " is a good age.")

if (age >= 16):
	print("You are old enough to drive.")	

else:
	print("You are not old enough to drive.")

e = input("So, " + n + " how are you today?")
print()

if (e == "good"):
	print("Thats good to hear.")

else:
	print("Oh thats interesting.")

print()

g = input("Do you have a favorite game?")

gg = input("What is it?")

if (g == "yes"):
	if(gg == "legend of zelda"):
		print("Oh I love that game.")
	elif(gg == "smash bros"):
		print("That's a great game")	
	else:
		print("That game is good, it's not my favorite though.")
else:
	print("Oh thats too bad.")			



ae = input("Anything else you want to say?")

if(ae == "no" or ae == "not really"):
	print("Oh ok, goodbye!")
	
elif(ae == "yes"):
	print("Sorry i really couldn't care less")

else:
	print("Sorry I'm running low on power, Goodbye.")
