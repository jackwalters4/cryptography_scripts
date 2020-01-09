#Jack Walters
#Script meant to convert letters to numbers and opposite for my Cryptography class
 
def convert_to_num(letter) :
	if (len(letter) > 1):
		return('Enter valid value')
	return ord(letter) - 97 #ord for ascii value of letter

def convert_to_letter(num) :
	num = int(num) % 26
	return chr(num + 97) #chr for letter from ascii value

val = input("Enter value to be converted ('quit' to quit) : ")

while (val != 'quit') :

	if (val.isalpha()) :
		print(convert_to_num(val.lower()))
	elif(val.isnumeric()) :
		print(convert_to_letter(val))
	else :
		print('Enter valid value')

	val = input("Enter value to be converted ('quit' to quit) : ")



