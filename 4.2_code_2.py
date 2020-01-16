nlist=[]
while(sum(nlist)<=100):
    n = int(input("Enter a number: "))
    nlist.append(n)
print("Sum: " + str(sum(nlist)))
print("Numbers Entered: " + str(len(nlist)))
