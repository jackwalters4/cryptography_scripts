#Jack Walters
#Script meant to convert letters to numbers and opposite for my Cryptography class
 
def convert_to_num(letter) :
	return ord(letter) - 97

def convert_to_letter(num) :
	num = int(num) % 26
	return chr(num + 97)

val = input("Enter value to be converted: ")

if (val.isalpha()) :
	print(convert_to_num(val.lower()))
else :
	print(convert_to_letter(val))



