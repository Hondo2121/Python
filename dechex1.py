# dechex1.py Kenny
def hexcon(num):
	HexString =""
	Key = "0123456789ABCDEF"	
	if(num //16 >= 1):
		HexString+=str(Key[num // 16])
		HexString+=str(Key[num % 16])
		num = num % 16
	else:
		HexString+=str(Key[num % 16])
		num = num % 16
	print(HexString)	
	
def main():	
	io=int(input("input a number lower than 255: "))
	hexcon(io)
main()
