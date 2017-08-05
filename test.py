import sys

args = sys.argv
if "-p" in args:
	print args.index("-p")
else:
	print "no argument given"