#!/usr/bin/env python
import sys
from urllib import urlopen
import bs4
from bs4 import BeautifulSoup as bs
import random
import json

SET_SEED = True
args = sys.argv
history = json.loads(open("seeds.json").read())
page_no = 0

#From seed history
if "-p" in args:
	_pIndex = args.index("-p")
	_record = int(args[_pIndex + 1]) + 1
	seed = history["seeds"][len(history["seeds"])-1+_record]["seed"]
	SET_SEED = False

while True:
	if SET_SEED:
		page_no = random.randint(1,10)
	#proxies = {'http': PROXY_IP:PORT_NO}
	page = urllib.urlopen('https://allpoetry.com/classics/famous_poems?page='+str(page_no))
	page_content = page.read()
	page_content = bs(page_content,"html.parser")
	divs = page_content.find_all("div", {"class":"details"})
	poem_index = random.randint(0,len(divs)-1)
	poem_link = (divs[poem_index].contents)[0].attrs['href']
	page = urllib.urlopen('https://allpoetry.com'+poem_link)
	if(divs):
		lines = divs.find_all("div")
		if SET_SEED:
			history["seeds"].append({'seed':seed})
			fs = open("seeds.json","w+")
			fs.write(json.dumps(history))
			fs.close()
		break

#Format title and poet
poet = poet.text.lstrip("\n")
poet = poet.lstrip(" ")
print "\t\t\t\t\t"+title.text+" \n\t\t\t\t\t\t\t-"+poet
print "\n"

#line number control
if "-l" in args:
	_lIndex = args.index("-l")
	_lLimit = int(args[_lIndex + 1])
	for line_number in range(0,min(len(lines),_lLimit+1)):
		print "\t\t\t\t\t"+lines[line_number].text
else:
	for line in lines:
		print "\t\t\t\t\t"+line.text