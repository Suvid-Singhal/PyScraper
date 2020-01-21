from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen
import re

link = input("Enter the URL: ")

html_page = urlopen(link)
soup = BeautifulSoup(html_page,features="lxml")

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
	path = urlparse(link.get('href')).path
	if path == '/':
		continue
	else:
		print(path)
