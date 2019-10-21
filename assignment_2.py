#Assigntment 2

a = int(input("Enter Side A : "))
b = int(input("Enter Side B : "))
c = int(input("Enter Side C : "))
d = int(input("Enter Side D : "))
e = int(input("Enter Side E : "))

a1 = int(a - c)
d1 = int(d - b - e)

ArS = float(a * b)  #big square
Ars = float(a1 * d1) #little square
Art = float(a1 * e / 2) #triangle

RoomArea = float(ArS + Ars + Art)

print("")
print(RoomArea)
