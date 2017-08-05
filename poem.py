#!/usr/bin/env python
import sys
from urllib import urlopen
from bs4 import BeautifulSoup as bs
import random


while True:
	seed = random.randint(43100,50000)
	page = urlopen("https://www.poetryfoundation.org/poems/"+str(seed))
	page_content = page.read()
	page_content = bs(page_content,"html.parser")
	divs = page_content.find("div", {"class":"o-poem"})
	title = page_content.find("h3", {"class":"c-hdgSans c-hdgSans_5 c-mix-hdgSans_blocked"})
	poet = page_content.find("span", {"class":"c-txt c-txt_attribution"})
	if(divs):
		lines = divs.find_all("div")
		break
poet = poet.text.lstrip("\n")
poet = poet.lstrip(" ")
print "\t\t\t\t\t"+title.text+" \n\t\t\t\t\t\t\t-"+poet
print "\n"

#Print line as per argv[1]/NULL
if len(sys.argv) == 1:
	for line in lines:
		print "\t\t\t\t\t"+line.text
else:
	_l = int(sys.argv[2])
	for line_number in range(0,min(len(lines),_l)):
		print "\t\t\t\t\t"+lines[line_number].text