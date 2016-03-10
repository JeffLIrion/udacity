#!/usr/bin/python
import sys
from datetime import datetime

# weekday = datetime.strptime(date, '%Y-%m-%d').weekday()

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 6:
        # print the weekday and the sale amount
        weekday = datetime.strptime(data[0], '%Y-%m-%d').weekday()
        print "{0}\t{1}".format(weekday, data[4])
