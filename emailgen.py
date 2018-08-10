# With Love by Thatyana Morales July 2018 
#
# python emailgen.py [list of names] [results file name] [domain] [email format]
# This is a script to be run on the command line
# This script is to create an email list given a list of users. It supports john.smith (first name + . + last name), and jsmith (first initial last name)
# Example:
# python emailgen.py names.txt results.txt company.com john.smith
# python emailgen.py users.txt results.csv company.net jsmith

import sys
import re

filename = sys.argv[1]
results = sys.argv[2]
domain = sys.argv[3]

fp = open(filename, "r")
fp2 = open(results, "w")

for line in fp:
	if line == '':
		break
	else:
		nameArray = re.split(' ', line)
		firstName = nameArray[0]
		lastName = nameArray[1]
		if sys.argv[4] == "john.smith": #firstname.lastname
			fp2.write((firstName + "." + lastName + "@" + domain + "\n").lower())
		elif sys.argv[4] == "jsmith": #firstInitial + LastName
			fp2.write((firstName[:1] + lastName + "@" + domain + "\n").lower())

fp.close()
fp2.close()
