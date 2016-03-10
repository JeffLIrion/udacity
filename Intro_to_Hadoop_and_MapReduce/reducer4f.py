#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

def reducer():
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    user = []
    
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 6 and len(data) != 10:
            # something is wrong
            pass
            
        # new user
        if user and user[0] != data[0]:
            user = data
            continue
            
        # posts by the user
        writer.writerow(data+user[2:])
        
        
if __name__=='__main__':
    reducer()
