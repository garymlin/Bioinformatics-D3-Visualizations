import itertools


twosides_smaller = open('twosides_every20.tsv','w')

with open("3003377s-twosides.tsv", 'r') as f:
    tenthlines = itertools.islice(f, 0, None, 20)
    for line in tenthlines:
    	twosides_smaller.write(line)

twosides_smaller.close()



