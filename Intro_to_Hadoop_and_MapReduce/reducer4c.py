#!/usr/bin/python

import sys

# the input is of the format: word \t node_id

old_word = None
count = 0
id_set = set()

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    # same word --> add to the count
    if old_word and old_word == data[0]:
        count += 1
        id_set.add(data[1].strip('"'))
        
    # new word
    else:
        # not the first word
        if old_word:
            print old_word, '\t', count, '\t', sorted(id_set)
            
        # reset the old_word and the count
        old_word = data[0]
        count = 1
        id_set = set()

# the last word
if old_word != None:
    print old_word, '\t', count, '\t', sorted(id_set)

