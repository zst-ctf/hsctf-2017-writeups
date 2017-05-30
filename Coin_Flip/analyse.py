#!/usr/bin/env python
import itertools

with open('data.txt', 'r') as myfile:
	data = myfile.read()
#data = '001111101011'

#http://stackoverflow.com/questions/23255222/split-when-character-changes-in-python
#split consecutive characters
split_list = ["".join(g) for k, g in itertools.groupby(data)]

#count len of each consecutive string and then increment dict count
dict_count = {}
for each in split_list:
	count = len(each)
	if count in dict_count:
		dict_count[count] += 1
	else:
		dict_count[count] = 1
## print dict_count

# http://stackoverflow.com/questions/16971502/joining-valuelist-from-key-value-in-dictionary
# http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
flag = (str( dict_count[key] ) for key in sorted(dict_count.iterkeys()))

print ', '.join(flag)
