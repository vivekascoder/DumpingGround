"""
Naem: reverse.py
Description: Algorithm for reverse cipher
Date: 22-Mar-2020
Author: vivekascoder
"""


def encrypt(text):
	"""
	It'll return the encrypted message using reverse cipher.
	NOTE: More features to be added.
		Like replacing the spaces with some other letter.
	"""
	return text[::-1]
def decrypt(cipher_text):
	"""
	It'll decrypt the message using reverse cipher
	"""
	return cipher_text[::-1]
