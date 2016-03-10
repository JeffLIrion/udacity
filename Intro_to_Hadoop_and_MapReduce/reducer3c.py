#!/usr/bin/python

import sys

sale = None
sales_value = 0.0
sales_count = 0

# Loop around the data
# It will be in the format key, val
# Where key is the store, val is the sale amount

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    (_, sale) = data_mapped
    sales_value += float(sale)
    sales_count += 1

if sale != None:
    print sales_value, "\t", sales_count

