# Advent of code Year 2021 Day 5 solution
# Author = David Myers
# Date = December 2020
import numpy as np
with open((__file__.rstrip("code.py")+"sample.txt"), 'r') as input_file:
    input = input_file.read()

input = input.strip().split('\n')
lines = [each.split(' -> ') for each in input]
points = [point.split(',') for line in lines for point in line]

points =[int(coord) for point in points for coord in point]

print(lines)
print(points)
x1,x2,y1,y2=[],[],[],[]

i=0
while i+4 < len(points):
    x1.append(i)
    y1.append(i+1)
    x2.append(i+2)
    y2.append(i+3)
    i+=4
print(x1,x2,y1,y2)



# print(coords1, coords2)
# for each in input:
#     print(each)

print("Part One : "+ str(None))



print("Part Two : "+ str(None))
