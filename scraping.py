"""
Name: scraing.py
Description: Used to extract the price from the given url
Author: @vivekascoder
"""

from requests_html import HTMLSession
import sys

def get_price(url):
	"""
	Argument: Url of the amazon product.
	Return: The prize string.
	"""
	session = HTMLSession()
	r = session.get(url)
	span_tag = r.html.find("span#priceblock_ourprice", first=True)
	price = span_tag.text
	return price

if __name__ == '__main__':
	print(get_price(sys.argv[1]))