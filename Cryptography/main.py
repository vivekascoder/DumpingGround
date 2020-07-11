"""
Name: main.py
Description: A interface or connector for all algorithm.
Date: 22-Mar-2020
Author: vivekascoder
"""

import sys
import rot13
import rot47
import reverse
import md5


"""
First argument denotes the algorithm: --rot13, --rot47
Second argument denotes the function: --encrypt, --decrypt, --bruteforce
Third argument denotes the plain text or cipher text: --text str
Forth argument denotes the key, if needed: --key str/int
...
"""

class message:
	output_info = "The message has been decrypted successfully."
	error_input = "Your input is out of our scope."
	extra_input_shell = "If you want to use the shell,\
	then only provide one parameter i.e --shell"


def shell():
	while True:
		print("Welcome to hidden.")
		print("[1] Reverse Cipher Encryption.")
		print("[2] ROT13 Encryption.")
		print("[3] ROT47 Encrytion.")
		print("[4] MD5 Hash Encryption.")
		print("[0] To exit from shell. ")
		print("")
		ch = int(input(">>> "))
		if ch == 0:
			break
		elif ch == 1:
			text = input("Enter the text: ")
			print(reverse.encrypt(text))
		# ...
		elif ch == 4:
			text = input("Enter the text: ")
			print(md5.encrypt(text))
		else:
			print(message.error_input)


if __name__ == "__main__":
	# Here comed the main program.
	if sys.argv[1] == "--shell" and len(sys.argv) == 2:
		shell()
	elif len(sys.argv) > 2 and sys.argv[1] == "--shell":
		print(message.extra_input_shell)
	elif sys.argv[1] == "--reverse":
		text = sys.argv[sys.argv.index('--text')+1]
		if "--encrypt" in sys.argv:
			output = reverse.encrypt(text)
			print(message.output_info)
			print(output)
	elif sys.argv[1] == "--md5":
		text = sys.argv[sys.argv.index('--text')+1]
		if "--encrypt" or "--generate" or "--hash" in sys.argv:
			output = md5.encrypt(text)
			print(message.output_info)
			print(output)