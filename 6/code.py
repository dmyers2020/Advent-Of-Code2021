# Advent of code Year 2021 Day 6 solution
# Author = David Myers
# Date = December 2020
import re
import math
from collections import defaultdict
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

    input = [re.findall('[\d]', line) for line in input]
    input = [list(map(int, line)) for line in input]

root = defaultdict()
for i in range(9):
    root[i] = input[0].count(i)

# print(f'original root:\n{root}')

def newRootGenerator (old_root):
    '''
    input: old_root dict()
    output: new_root dict()
    '''
    list_root=list(old_root.items()) #list of key value pairs from dict
    new_root = defaultdict()
    for key, value in list_root[:8]:
        # new_root[8] = list_root[0][1]
        new_root[key] = list_root[key+1][1] #shifts the count of 8s to become the count of 7s; etc.
        # new_root[8]
    new_root[8]=list_root[0][1] #adds an 8 for every 0 in the last gen
    new_root[6]+=list_root[0][1] #all 6s become 0s, add to 7s that became 0s.
    return new_root

for gen in range(256):
    ''' for part 1 - run this to gen 80, vice 256'''
    root = newRootGenerator(root)
    # print(root)

print(sum(root.values()))
