#!/usr/bin/python

import itertools

array = [[1,2,3],
       [8,9,4],
       [7,6,5]]

def TransposeAndFlip(array):
    while array:
        yield array[0]
        array = list(reversed(zip(*array[1:])))

print list(itertools.chain(*TransposeAndFlip(array)))
