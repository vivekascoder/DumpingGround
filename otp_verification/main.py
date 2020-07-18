#################################
# OTP Verification Console Based
# Author: @vivekascoder
# Service Provider: 2factor
# Pricing: 0.18 INR/OTP
# TextEditor: Sublime
# AutoCompletion: Jedi
# Color Theme: Vim BlackBoard
# Theme: Guna
#################################
"""
A Console based application to demostrate the use the OTP system.
"""

import requests
import sys

# The below token needs to be hidden somewhere...
auth_token = "YOUR API_KEY OR AUTH_TOKEN COMES HERE"

def send_otp(auth_token, phone_no):
	"""
	This function is used to send the otp to a particular
	phone no, using requests module of python.
	NOTE: phone_no needs to be an indian no. for trial account of
		  2factor, so don't need to provide the contry code.
	"""
	r = requests.get(f"https://2factor.in/API/V1/{auth_token}/SMS/{phone_no}/AUTOGEN")
	if r.status_code == 200 and r.json()['Status'] == "Success":
		session_id = r.json()['Details']
		return session_id
	else:
		print("[+]: While sending the OTP.")

def verify_otp(auth_token, otp_input, session_id):
	"""
	This function will verify the otp with session id.
	"""
	r = requests.get(f"https://2factor.in/API/V1/{auth_token}/SMS/VERIFY/{session_id}/{otp_input}")
	if r.json()['Status'] == 'Success' and r.json()['Details'] == "OTP Matched":
		return True
	else: 
		return False

if __name__ == '__main__':
	phone_no = input("[+] Enter phone no: ")
	session_id = send_otp(auth_token, phone_no)
	otp_input = input("[+] Enter the recieved OTP: ")
	if verify_otp(auth_token, otp_input, session_id) == True:
		print("The OTP is verified Successfully!!")
	else:
		print("Wrong OTP.")



