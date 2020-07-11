#!/usr/bin/python3 

from bs4 import BeautifulSoup as bs4
import requests
import json
movieId = 'tt9680440'
url = 'https://www.imdb.com/title/'+movieId+'/'
response = requests.get(url)
responseHtml = bs4(response.content,'lxml')
jsonResponse = responseHtml.find(attrs={'type':'application/ld+json'})
print(jsonResponse.getText())
str(jsonResponse)
