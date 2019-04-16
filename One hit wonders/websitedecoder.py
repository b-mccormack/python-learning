#Decode a website

import requests
from bs4 import BeautifulSoup

targetURL = 'http://abc.net.au/news'
result = requests.get(targetURL)
result_html = result.text
soup = BeautifulSoup(result_html, 'html.parser')

listOfTitles = []

for titles in soup.find_all('h3'):
    if titles.a:
        listOfTitles.append(titles.a.text)

titlesSorted = []

for num in listOfTitles:
	if titlesSorted.count(num) < 1:
		titlesSorted.append(num)

newLines = "\n".join(titlesSorted)

writefile = open("ABCHeadlines.txt","w+")
writefile.write(newLines)
writefile.close()