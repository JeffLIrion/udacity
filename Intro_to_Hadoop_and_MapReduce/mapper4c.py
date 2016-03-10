#!/usr/bin/python
import sys
import csv
import re

# split on white space and: .,!?:;"()<>[]#$=-/

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    words = re.split('\s*[,.!?:;"()<>\[\]#$=\-/\s]+\s*',line[4].lstrip().lower()+' ')
    #print words
    for word in words[:-1]:
        #writer.writerow([word, line[0]])
        print word, '\t', line[0]
