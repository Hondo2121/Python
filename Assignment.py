fName = input("What is your first name? ")
lName = input("What is your last name?")
ID = int(input("Student ID: "))
n=1
inputclasses = []
roomnums=[]
print("*************************************************")
print("*                                               *")
print("*\t" + lName + ", " + fName + "\t\t" + "ID: " + str(ID)+ "\t*")
print("*                                               *")
print("*************************************************")
print("*                                               *")
while(inputclasses.count("stop")  == 0):
	temp = input("Enter the next class, Stop to end: ")
	inputclasses.append(temp)
	if(inputclasses.count("stop")  == 0):
		temp = int(input("Enter the room number: "))
		roomnums.append(str(temp))
		n+=1
for i in range(n):
	if(i!=0):
		print("*\tBlock "+str(i) + ": " + inputclasses[i-1] + "\tRoom: " + str(roomnums[i-1]) + "\t*")
print("*                                               *")
print("*************************************************")
print("*                                               *")
print("*************************************************")
