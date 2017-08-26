#!/usr/bin/env python
import sys
import urllib
import bs4
from bs4 import BeautifulSoup as bs
import random
import json

args = sys.argv
history = json.loads(open("seeds.json").read())

def is_valid_line(line):
	if type(line) == bs4.element.NavigableString:
		return True
	return False

def get_poem():
	PASS = True
	while PASS:
		page_no = random.randint(1,10)
		page = urllib.urlopen('https://allpoetry.com/classics/famous_poems?page='+str(page_no))
		page_content = page.read()
		page_content = bs(page_content,"html.parser")
		divs = page_content.find_all("div", {"class":"details"})
		poem_index = random.randint(0,len(divs)-1)
		poem_link = (divs[poem_index].contents)[0].attrs['href']
		poem_page = urllib.urlopen('https://allpoetry.com'+poem_link)
		poem_page_content = poem_page.read();
		poem_page_content = bs(poem_page_content,"html.parser")
		lines = poem_page_content.find('div',{'class':'preview poem_body'})
		if len(lines) != 0:
			PASS = False		
	title = ((poem_page_content.find('h1',{'class':'title'})).contents)[0].contents
	poet = ((poem_page_content.find('span',{'class':'n'})).contents)[0].contents
	del lines[-1]
	poem = []
	for line in lines:
		if is_valid_line(line):
			poem.append(line)
	return title, poet, poem

def print_poem(title, poet, poem):
	print title[0]
	print " - By "+poet[0]
	for line in poem:
		print line

title, poet, poem = get_poem()
print_poem(title, poet, poem)

# get_poem()


# #From seed history
# if "-p" in args:
# 	_pIndex = args.index("-p")
# 	_record = int(args[_pIndex + 1]) + 1
# 	seed = history["seeds"][len(history["seeds"])-1+_record]["seed"]
# 	SET_SEED = False

# while True:
	
# 	print page.read()
# 	if(divs):
# 		lines = divs.find_all("div")
# 		if SET_SEED:
# 			history["seeds"].append({'seed':seed})
# 			fs = open("seeds.json","w+")
# 			fs.write(json.dumps(history))
# 			fs.close()
# 		break

# exit()

# #Format title and poet
# poet = poet.text.lstrip("\n")
# poet = poet.lstrip(" ")
# print "\t\t\t\t\t"+title.text+" \n\t\t\t\t\t\t\t-"+poet
# print "\n"

# #line number control
# if "-l" in args:
# 	_lIndex = args.index("-l")
# 	_lLimit = int(args[_lIndex + 1])
# 	for line_number in range(0,min(len(lines),_lLimit+1)):
# 		print "\t\t\t\t\t"+lines[line_number].text
# else:
# 	for line in lines:
# 		print "\t\t\t\t\t"+line.text