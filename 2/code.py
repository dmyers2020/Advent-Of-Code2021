# Advent of code Year 2021 Day 2 solution
# Author = David Myers
# Date = December 2020 

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()
    input = [line.split() for line in input]

    # print(input[0][0]=='forward')

def part_1(input):
    horizontal = 0
    depth = 0
    i = 0
    for command in input:

        if input[i][0] == 'forward':
            horizontal+=int(input[i][1])
        if input[i][0] == 'down':
            depth += int(input[i][1])
        if input[i][0] == 'up':
            depth -= int(input[i][1])
        i+=1
    return(horizontal*depth)

def part_2(input):
        horizontal = 0
        depth = 0
        aim = 0
        i = 0
        for command in input:

            if input[i][0] == 'forward':
                horizontal+=int(input[i][1])
                depth += aim*int(input[i][1])
            if input[i][0] == 'down':
                aim += int(input[i][1])
            if input[i][0] == 'up':
                aim -= int(input[i][1])
            i+=1
        return(horizontal*depth)


print("Part One : "+ str(part_1(input)))
print("Part Two : "+ str(part_2(input)))
