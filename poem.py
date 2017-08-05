#!/usr/bin/env python
import sys
from urllib import urlopen
from bs4 import BeautifulSoup as bs
import random
import json

SET_SEED = True
args = sys.argv
history = json.loads(open("seeds.json").read())
seed = 0

#From seed history
if "-p" in args:
	_pIndex = args.index("-p")
	_record = int(args[_pIndex + 1]) + 1
	seed = history["seeds"][len(history["seeds"])-1+_record]["seed"]
	SET_SEED = False

while True:
	if SET_SEED:
		seed = random.randint(43100,50000)
	page = urlopen("https://www.poetryfoundation.org/poems/"+str(seed))
	page_content = page.read()
	page_content = bs(page_content,"html.parser")
	divs = page_content.find("div", {"class":"o-poem"})
	title = page_content.find("h3", {"class":"c-hdgSans c-hdgSans_5 c-mix-hdgSans_blocked"})
	poet = page_content.find("span", {"class":"c-txt c-txt_attribution"})
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