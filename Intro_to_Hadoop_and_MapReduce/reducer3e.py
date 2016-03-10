#!/usr/bin/python

import sys

key = None
key_count = 0

# Loop around the data
# It will be in the format key, val
# Where key is the store, val is the sale amount

for line in sys.stdin:
    newkey = line.strip()
    
    # same key --> add to the count
    if key and key == newkey:
        key_count += 1
    
    # new key --> print old key & count, then reset key & count
    else:
        # print the old key & count as long as it's not the first line
        if key:
            print key, "\t", key_count
            
        key = newkey
        key_count = 1

# print the last key & count
if key != None:
    print key, "\t", key_count

