"""
Author: Sanil Sampat
Date:   11 / 17 / 2012

Opens a file, counts the number
of occurences of each word, and
outputs the info to a new file
sorted in descending order by count.
Assumes one word per line.

Usage: $ python script.py filename.txt
"""

import sys
from collections import defaultdict 

# some quick error checking, not robust
if len(sys.argv) != 2:
	print "Please supply a file name as the only agrument"
	print "Usage: $ python script.py filename.txt"
	sys.exit("Terminating...")

arg = sys.argv[1]
	
try:
	inFile = open(arg, 'r')
except IOError:
	sys.exit("Terminating... cannot open %s" % arg)

# Python Docs 8.3.3.1 for more details
d = defaultdict(int)

for line in inFile.readlines():
	d[line.rstrip()] +=1 # strip /n, append, increment count

inFile.close()

# sort by count, reverse for descending order	
result = sorted(d.items(), key=lambda word: word[1], reverse=True) 

try:
	outFile = open('output.txt', 'w+')
except IOError:
	sys.exit("Terminating... cannot open/create output file")	

print "Writing word occurences to output.txt..."

for word, count in result:
	outFile.write("%s: %d\n" % (word, count))

outFile.close()

print "Done!"