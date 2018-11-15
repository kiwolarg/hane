import urllib
import urllib2
import requests
from array import *
from bs4 import BeautifulSoup
import sys



flag = 0
result = []
query = sys.argv[1].strip("\"").replace(" ","+")
url = "https://www.urbandictionary.com/define.php?term=" + query
hdr = {'User-Agent':'Mozilla/5.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

req = urllib2.Request(url, headers=hdr)
page = urllib2.urlopen(req)

html = page.read()
soup = BeautifulSoup(html,"lxml")

#print len(result)

result = soup.findAll('div',attrs={'class':'meaning'})

print result[0].text
	
'''	
else : 
	print ('test')


for parentDiv in soup.findAll('div',attrs={'class':'meaning'}):
	flag = 1
	result.append(parentDiv.text)

if flag == 0:
	print "eh...."
	
if flag == 1:
	print result[0]
	
'''