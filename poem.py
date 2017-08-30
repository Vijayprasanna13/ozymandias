#!/usr/bin/env python
import sys
import urllib
import bs4
from bs4 import BeautifulSoup as bs
import random
import json

args = sys.argv
DEBUG = False


def add_to_history(poem_link):
	history = json.loads(open("history.json").read())
	print history
	fs = open('history.json','rw+')
	history.append({"peom_link":poem_link})
	fs.write(json.dumps(history))
	fs.close()

def is_valid_line(line):
	if type(line) == bs4.element.NavigableString:
		return True
	return False

def get_poem(use_history = False):
	PASS = True
	while PASS:
		if use_history:

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
		if DEBUG:
			print 'https://allpoetry.com/classics/famous_poems?page='+str(page_no)
			print divs
			#print 'https://allpoetry.com'+poem_link
		if len(lines) != 0:
			PASS = False		
	
	title = ((poem_page_content.find('h1',{'class':'title'})).contents)[0].contents
	poet = ((poem_page_content.find('span',{'class':'n'})).contents)[0].contents
	del lines[-1]
	poem = []
	for line in lines:
		if is_valid_line(line):
			poem.append(line)

	if len(poem) == 0:
		lines = (lines.find('p')).contents
		for line in lines:
			if is_valid_line(line):
				poem.append(line)
	add_to_history(poem_link)
	return title, poet, poem

def print_poem(title, poet, poem, options):
	print title[0]
	print " - By "+poet[0]

	_line_limit = len(poem) if options['line_limit'] == None else options['line_limit']
	
	for i in range(0,min(len(poem), _line_limit)):
		print poem[i]

options = {}

#line control
if "-l" in args:
	_l_index = args.index("-l")
	_l_limit = int(args[_l_index + 1])
	options['line_limit'] = _l_limit
else:
	options['line_limit'] = None

#history
if "-h" in args:
	_h_index = args.index("-h")
	_h_val = int(args[_h_index + 1])
	options['history'] = _h_val
else:
	options['history'] = None

title, poet, poem = get_poem()
#print_poem(title, poet, poem, options)

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