'''
Takes a string of data with even length from standard input (stdin).
Ignores all newlines from stdin and gets the actual data line.

'''

import os
import sys
import fileinput

data = ""	# The data to loop over

for line in fileinput.input():
	line = line.rstrip()
	if line != "":
		data = line
		
i = 0
result = ""
for start in range(0, len(data), 2):
	charecters = data[start:start+2]
	if i % 16 == 0 and i != 0:
		result = result + "\n"
	result = result + str(charecters) + " "
	i += 1

print(result)
