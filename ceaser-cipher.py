#!/usr/bin/python3

"""
Name: [0001]Implementation of ceaser cipher.
Date: 12 May, 2020
Author: vivekascoder
"""

import sys

def encrypt(text, key):
	"""
	65-90: A-Z
	97-122: a-z
	48-57: 0-9
	Formula: 
		Uppercase: chr(ord(char) + key-65) % 26 + 65
		Lowercase: chr(ord(char) + key-97) % 26 + 97
	"""
	encrypted_text = ""
	for i in text:
		if i.isupper():
			encrypted_text += chr((ord(i) + key-65) % 26 + 65)
		else:
			encrypted_text += chr((ord(i) + key-97) % 26 + 97)
	return encrypted_text

if __name__ == "__main__":
	if "--encrypt" and "--text" and "--key" in sys.argv:
		text = sys.argv[sys.argv.index('--text')+1]
		key = sys.argv[sys.argv.index('--key')+1]
		print("[+] ", encrypt(text, int(key)))
