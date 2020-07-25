#!/usr/bin/python3

# ############################################################
# This script will scrap the contributers of a python module.
# Author: @vivekascoder
# Date: 25 July, 2020
# ############################################################

"""
[1]: pypi
[2]: github, ...
"""

from requests_html import HTMLSession
import sys
from terminaltables import AsciiTable

module_name = sys.argv[1]

def pypi_url(module_name):
	"""
	This will return the search result of a module
	on pypi.org website.
	"""
	return f"https://pypi.org/project/{module_name}/"

def contributers_url(github_url):
	if github_url[-1] != '/':
		github_url += '/'
	return f"{github_url}graphs/contributors"

print("BOT: STARTING SESSION ... ["+module_name+"]")
session = HTMLSession()
r = session.get(pypi_url(module_name))
li_s = r.html.find("div.sidebar-section ul.vertical-tabs__list li a[rel='nofollow']", first=False)

for li in li_s:
	if "github." in li.attrs['href']:
		github_url = li.attrs['href']
		break

print("BOT: FETCHING GITHUB URL => ",github_url)
r = session.get(contributers_url(github_url))
r.html.render(sleep=5)
a_s = r.html.find("a.text-normal[data-hovercard-type='user']", first=False)
print("BOT: FETCHING CONTRIBUTORS...")
data = [["Contributors", "Github URL"]]
for a in a_s:
	data.append([a.text, "github.com" +a.attrs['href']])
tbl = AsciiTable(data)
print(tbl.table)
