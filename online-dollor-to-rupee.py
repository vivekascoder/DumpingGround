#!/usr/bin/python3
"""
Name: price.py
Description: A CLI utility to get dollor price in rupees.
Date: 22-Mar-2020
Author: vivekascoder
"""

import sys
from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()
async def getPrice():
	data = await asession.get("https://www.google.com/search?client=firefox-b-d&q="+(sys.argv[2])+"%24+in+rupees")
	ans = data.html.find("span[class='DFlfde SwHCTb']", first=True)
	print(ans.text, "rupees only.")

if sys.argv[1] == "--value" and len(sys.argv) == 3:
	asession.run(getPrice)
