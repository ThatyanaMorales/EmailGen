# EmailGen
This script is to create an email list given a list of users. The command-line layout is detailed below:

python emailgen.py {list of names} {results file name} {domain} {email format}

It supports john.smith (first name + . + last name), and jsmith (first initial last name)
Example:

python emailgen.py names.txt results.txt company.com john.smith
python emailgen.py users.txt results.csv company.net jsmith

Note: the last parameter must be in terms of John Smith (so the parameter can only either be john.smith or jsmith)

The text file with the list of names should only be first and last name and each entry separated by a newline (middle names are not yet supported):

Example: names.txt

Perry Leonard
Pamela Collins
Mary Wynn
Inez Wagner
Suzette Taylor
...

Running the following:

python emailgen.py names.txt results.csv company.net jsmith

Will return the following:

pleonard@company.net
pcollins@company.net
mwynn@company.net
iwagner@company.net
staylor@company.net
