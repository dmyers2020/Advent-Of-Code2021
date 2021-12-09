# Advent of code Year 2021 Day 5 solution
# Author = David Myers
# Date = December 2020
import numpy as np
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = input.strip().split('\n')
lines = [each.split(' -> ') for each in input]
points = [point.split(',') for line in lines for point in line]

points =[int(coord) for point in points for coord in point]

x1s,x2s,y1s,y2s=[],[],[],[]

i=0
while i+4 <= len(points):
    x1s.append(points[i])
    y1s.append(points[i+1])
    x2s.append(points[i+2])
    y2s.append(points[i+3])
    i+=4

# grid of zeros of biggest x= num_cols by y=num_rows
grid = np.zeros((max(max(y1s,y2s))+2,max(max(x1s,x2s))+1), dtype=int)
# grid = np.zeros((1000,1000), dtype=int)

a = np.array([x1s,y1s,x2s,y2s])
a=a.transpose() #swap rows to cols
# print(a)
for line in a:
    x1,y1,x2,y2 = line[0], line[1], line[2], line[3]
    if x1==x2:
        ysmall, ybig = min(y1,y2), max(y1,y2)
        #assign value at col x for all rows y1 THROUGH y2 (thus the +1)
        for i in range(ysmall,ybig+1):
            grid[i][x1] +=1
    elif y1==y2:
        xsmall, xbig = min(x1,x2), max(x1,x2)
        grid[y1][xsmall:xbig+1] +=1

danger_points = np.sum(grid >1)
print('Part 1:' , danger_points)
