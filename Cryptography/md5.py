"""
Name: md5.py 
Description: A MD5 hash generator program using 'hashlib'
Date: 22-Mar-2020
Author: vivekascoder. 
"""

from hashlib import md5

def encrypt(text):
	"""
	Description: 
		This function is used to generate the MD5 hash using hashlib library.

	Arguments:
		arg1(text): A string to generate the md5 hash.

	Returns:
		str: A string representing the MD5 generated hash.
	"""
	hash = md5(text.encode('ascii'))
	return hash.hexdigest()