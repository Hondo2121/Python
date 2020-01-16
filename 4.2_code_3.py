plist = []
print("User enters: ")
while(plist.count("rock")==0):
	p=input("")
	plist.append(p)
for n in range(len(plist)-1):
	print("You have a " + plist[n]+ " with a total of " + str(n+1)+ " pet(s)")
