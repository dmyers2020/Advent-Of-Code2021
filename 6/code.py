# Advent of code Year 2021 Day 6 solution
# Author = David Myers
# Date = December 2020
import re
import math
with open((__file__.rstrip("code.py")+"sample.txt"), 'r') as input_file:
    input = input_file.readlines()

    input = [re.findall('[\d]', line) for line in input]
    input = [list(map(int, line)) for line in input]

for line in input:
    print(line)

# default dic for initial seed

# for each in initial seed
    # default dic
        # for key in initial dic
            # decrement key; keep same value from last step
        # num of 6s += num 0s from last step
        # num of 8s += num of 0s from last step
# return sum of values in new_defaultdic


print("Part One : "+ str(None))



print("Part Two : "+ str(None))
