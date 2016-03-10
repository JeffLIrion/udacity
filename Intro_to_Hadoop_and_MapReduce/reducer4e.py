#!/usr/bin/python

import sys

# the input is of the format: day_of_week \t sale_amount

old_day = None
sales = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    # same day --> add to the sales
    if old_day and old_day == data[0]:
        sales += float(data[1])
        
    # new word
    else:
        # not the first word
        if old_day:
            print old_day, '\t', sales
            
        # reset the old_word and the sales
        old_day = data[0]
        sales = float(data[1])

# the last word
if old_day != None:
    print old_day, '\t', sales

