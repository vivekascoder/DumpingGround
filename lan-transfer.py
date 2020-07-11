#!/usr/bin/env python3
import os
from requests_html import HTMLSession

url = input(">>-> Enter The URL With PORT: ")

if url[:-1] != '/':
	url += '/'
session = HTMLSession()
data = session.get(url)
link_elements = data.html.find("li a")
links = {}
print("\n", "="*10)
for link_element in link_elements:
	links[link_elements.index(link_element) + 1] = link_element.attrs['href']
	print(link_elements.index(link_element) + 1, " : ", link_element.attrs['href'])
print("\n", "="*10)

_from = int(input(">>-> From: "))
_to = int(input(">>-> To: "))

for index in range(_from, _to + 1):
	os.system("wget " + url + links[index])
print("Everything You Want Is Downloaded Now {*_*}")
