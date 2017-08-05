#!/usr/bin/env python
from urllib import urlopen
from bs4 import BeautifulSoup as bs
import random

while True:
	seed = random.randint(43100,50000)
	page = urlopen("https://www.poetryfoundation.org/poems/"+str(seed))
	page_content = page.read()
	page_content = bs(page_content,"html.parser")
	divs = page_content.find("div",{"class":"o-poem"})
	title = page_content.find("h3",{"class":"c-hdgSans c-hdgSans_5 c-mix-hdgSans_blocked"})
	poet = page_content.find("span",{"class":"c-txt c-txt_attribution"})
	if(divs):
		lines = divs.find_all("div")
		break

print "\t\t"+title.text+" "+poet.text.lstrip(" ")
for line in lines:
	print line.text