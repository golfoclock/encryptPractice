result = ''
message = ''
choice = ''

while choice != 0:
	choice = input("\nWould you like to encrypt or decrypt the message?\nEnter 1 to encrypt, or 2 to decrypt. Enter 0 to exit program.")

	if choice == '1':
		message = input("Enter message for encryption:")
		for i in range(0, len(message)):
			result = result + chr(ord(message[i]) - 2)
			