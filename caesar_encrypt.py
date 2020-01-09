#Jack Walters
#Script to Encrypt a message with a given Caesar Cipher

from convert import convert_to_num, convert_to_letter #my helper script

def encrypt(msg, shift) :
	cipher = [encrypt_letter(i.lower(),shift) for i in msg]
	return ''.join(cipher)

def encrypt_letter(letter, shift) :
	if (letter != " "):
		return convert_to_letter(convert_to_num(letter) + convert_to_num(shift)) 
	return " "


if __name__ == '__main__':
	
	msg = input("Enter plaintext you wish to be encrypted: ")
	shift = input("Enter letter value of Caesar Cipher: ").lower()

	print("Ciphertext: " + encrypt(msg, shift))