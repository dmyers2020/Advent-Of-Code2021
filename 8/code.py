# Advent of code Year 2021 Day 8 solution
# Author = David Myers
# Date = December 2020
import re
from collections import defaultdict
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split('\n')
    # input = input[:-1] #(this was sooooo annoying that they didn't format the sample like they did the input)
    line = [line.split(' | ') for line in input]
    inputs = [input[0].split(' ') for input in line]
    outputs = [x[1].split(' ') for x in line]
    z  = zip(inputs, outputs)
# digitPatternLengths = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
# digitPatternsTrue = {0:'abcefg', 1:'cf', 2:'acdeg', 3:'acdfg', 4:'bcdf', 5:'abdgf', 6:'abdefg', 7:'acf', 8:'abcdefg', 9:'abcdfg'}
# for key in digitPatternsTrue.keys():
#         digitPatternsTrue[key] = {str(letter) for letter in digitPatternsTrue[key]}

def out_value (d,output):
    """
    (d): a dict with keys for digits 0:9 and values of their scrambled 7-segment codes
    (output): a list of length 4, each item is a 7-segment code

    (out_value): a four-digit integer constructed from the (4) 7-segment codes
    """
    out_value = ''
    for each in output:
        odigit = digitSegmentizer(each)
        # print(odigit)
        for key_i, value_i in d.items():
            # print(f'digit to decode: {odigit}\n possible match: {value_i} \n value if matched: {key_i}')
            if value_i == odigit:
                # print(f'o_digit:{odigit} \nsegment:{value_i} \nresult:{key_i}')
                out_value +=str(key_i)
                # print(out_value)
    return out_value


def digitSegmentizer (input):
    return {str(letter) for letter in input}

running_sum = 0

for input, output in z:
    input.sort(key = len)
    d = defaultdict()
    for each in input:
        digit = digitSegmentizer(each)
        segments = {str(letter) for letter in digit}
        if len(digit) == 2:
            d[1] = segments             #1
        elif len(digit) == 3:
            d[7] = segments             #7
        elif len(digit) == 4:
            d[4] = segments             #4
        elif len(digit) == 7:
            d[8] = segments             #8
        elif len(digit) == 5:
            if (d[4]-d[1]).issubset(segments):
                d[5] = segments         #5
            elif len(digit-d[4]) == 2:
                # print(f'HELLLLLLO \n{digit} \n{d[4]} \n{digit-d[4]}')
                d[3]=segments           #3
            else: d[2]=segments          #2
        elif len(digit) ==6:
            if len(digit-d[4])==2:
                d[9] = segments         #9
            elif len(digit-d[7])==3:
                d[0] = segments         #0
            else: d[6] = segments        #6

        # digits decoded: find the related output, decode, add to sum
    # print(input)
    # print(output)
    # print(d)
    running_sum+=int(out_value(d,output))
print(running_sum)

            # running_sum += int(out_value)

# print(running_sum)

uni = 0
for out in outputs:
    for digit in out:
        if len(digit) in [2,3,4,7]:
            uni +=1

print("Part One : "+ str(uni))
print("Part Two : "+ str(None))


'''
# determine the segment differences between every digit:
for key_i, value_i in digitPatternsTrue.items():
    for key_j, value_j in digitPatternsTrue.items():
        if len(value_i)>len(value_j):
            delta = value_i - value_j
            # if len(delta) ==1:
            if len(delta)==1:
                print(f'{key_i} - {key_j} = {delta}')
        elif len(value_j)>len(value_i):
            delta = value_j-value_i
            if len(delta)==1:
                print(f'{key_j} - {key_i} = {delta}')
# print(inputs[0])
test = inputs[0]
test.sort(key = len)
'''
