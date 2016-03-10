#!/usr/bin/python

import sys

path = None
path_count = 0

# Loop around the data
# It will be in the format key, val
# Where key is the store, val is the sale amount

for line in sys.stdin:
    newpath = line.strip()
    
    # same path --> add to the count
    if path and path == newpath:
        path_count += 1
    
    # new path --> print old path & count, then reset path & count
    else:
        # print the old path & count as long as it's not the first line
        if path:
            print path, "\t", path_count
            
        path = newpath
        path_count = 1

# print the last path & count
if path != None:
    print path, "\t", path_count

