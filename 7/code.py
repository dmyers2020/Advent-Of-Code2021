# Advent of code Year 2021 Day 7 solution
# Author = David Myers
# Date = December 2020
import pandas as pd
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().strip().split(',')
input = list(map(int, input))

input.sort()
low, hi = min(input), max(input)

from collections import defaultdict

import math

freq = defaultdict(int)
for each in input:
    freq[each]+=1

keys, values  = list(freq.keys()), list(freq.values())

keyval = list(zip(keys,values))

currcost = 100**10
currcosti = 0

def sumOfSeqInts (n):
    nover2 = n/2
    if n%2 == 0:
        #n is even
        result = nover2*(n+1)
    else:
        result = math.floor(nover2)*(n+1) + math.ceil(nover2)
    return result

for i in range(low, hi):
    cost = 0
    for key, val in keyval:
        #mod for part2
        steps = abs(i-key)
        cost += sumOfSeqInts(steps)*val

    if cost < currcost:
        currcost = cost
        currcosti = i
print(currcost, currcosti)


print("Part One : "+ str(None))



print("Part Two : "+ str(None))
