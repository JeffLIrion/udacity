#!/usr/bin/python

import sys

old_store = None
max_sale = 0

# Loop around the data
# It will be in the format key, val
# Where key is the store, val is the sale amount

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    (store, sale) = data_mapped
    sale = float(sale)

	# if it's a new store (and not the first store)
    if old_store and old_store != store:
        print old_store, "\t", max_sale
        old_store = store;
        max_sale = sale
        
    # if it's the same store
    else:
    	old_store = store
        if sale > max_sale:
        	max_sale = sale

if old_store != None:
    print store, "\t", max_sale

