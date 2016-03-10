#!/usr/bin/python

import sys

key = None
key_count = 0
max_key = None
max_count = 0

# Loop around the data
# It will be in the format key, val
# Where key is the store, val is the sale amount

for line in sys.stdin:
    newkey = line.strip()
    
    # same key --> add to the count
    if key and key == newkey:
        key_count += 1
    
    # new key
    else:
        # compare the last key_count to max_count
        if max_count < key_count:
            max_count = key_count
            max_key = key
             
        # reset the key and the count
        key = newkey
        key_count = 1
    
# print the maximum key_count and its key
if key != None:
    print max_key, "\t", max_count

