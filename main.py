print("0:Exit\n")
print("1:Binary to decimal\n")
print("2:Decimal to binary\n")
print("3:Hexadecimal to binary\n")
print("4:Binary to text\n")
print("5:Text to binary\n\n\n")

def binToDec(binary):
	decimal = 0
	exponent = 0
	reversedBinary = binary[::-1]
	for number in reversedBinary:
		if number=="1":
			decimal += 2**exponent
			exponent+= 1
		elif number=="0":
			exponent+= 1
	return decimal		
		
	
def decToBin(decimal):
	binary = str(bin(decimal))
	formattedBinary = binary[2:]
	return formattedBinary

def hexToBin(hexadecimal):
	return format(int(hexadecimal, 16), "040b")
	
def binaryToText(binaryUser):
	binaryArray = binary.split()
	decimal = 0
	exponent = 0
	text = ""
	for binary in binaryArray:
		for number in binary:
			if(number=="1"):
				decimal += 2**exponent
				exponent+= 1
			elif(number=="0"):
				exponent+= 1
		text += chr(decimal)
	return text
	
def textToBinary(text):
	text.encode("ascii")
	
	

while True:
	option = int(input("Pick an option: "))
	if option==0:
		break
	elif option==1:
		userBinary = str(input("Enter binary value: "))
		print(binToDec(userBinary))
	elif option==2:
		userDecimal = int(input("Enter decimal value: "))
		print(decToBin(userDecimal))
	elif option==3:
		userHex = str(input("Enter hexadecimal value: "))
		print(hexToBin(userHex))
	elif option==4:
		userBinary = str(input("Enter binary value: "))
		print(binaryToText(userBinary))
    elif option==5:
    	userText = str(input("Enter text: "))
	else:
		print("Wrong input")
    	
