# Advent of code Year 2021 Day 3 solution
# Author = David Myers
# Date = December 2020
# started at 2200 exactly
with open((__file__.rstrip("code.py")+"sample.txt"), 'r') as input_file:
    input = input_file.read().splitlines()

# gamma rate = MOST COMMON BIT IN THE CORRESPONDING POSITION
# check the first index of all the lines, if there are more 1's than 0's,
# the first bit of the gamma rate is 1. repeat for next index, if more 0's than 1's,
# then the second bit of the gamma rate is 0.
# FOR SAMPLE: the gamma rate is 10110; or 22 in decimal.

# epsilon is the opposite; so use the least common bit.
# FOR SAMPLE:  EPSILON RATE IS 01001 OR 9

#  FINAL ANSER IS 22*9; 198
# I'll need to look up a binary->decimal function

def part_1 (input):
    gamma = [0]*len(input[0])
    epsilon = [0]*len(input[0])
    zeros = ones = 0 #count of each bit value in the original binary number position j
    for j in range(0,len(input[0])): #check each bit position


        for i in range(0,len(input)): #check each binary number

            # print(i,j,input[i][j])
            if int(input[i][j])==0: ones +=1
            else: zeros +=1

        if ones > zeros:
            gamma[j] = 1
            epsilon[j]=0
        elif zeros > ones:
            gamma[j]=0
            epsilon[j]=1

        print(f'ones: {ones}, zeros: {zeros}')
        print(f'      gamma: {gamma}')
        print(f'    epsilon: {epsilon}')
        zeros = ones = 0

    # my dumbass approach to converting a list of 0's and 1's to decimal
    gamma_dec = 0
    epsilon_dec = 0
    j=len(gamma)-1
    for i in range(0,len(gamma)):
        gamma_dec += int(gamma[i])*(2**j)
        epsilon_dec += epsilon[i]*(2**j)
        j-=1

    return gamma_dec*epsilon_dec


def part_2 (input):
    gamma = [0]*len(input[0])
    epsilon = [0]*len(input[0])
    zeros = ones = 0 #count of each bit value in the original binary number position j
    for j in range(0,len(input[0])): #check each bit position
        for i in range(0,len(input)): #check each binary number

            # print(i,j,input[i][j])
            if int(input[i][j])==0: ones +=1
            else: zeros +=1
        # print(j)
        if ones > zeros: #now, if there are more 1s than 0s we need to trim the input, and recurse.
            # I've got to figure out how to remove list items from the input by checking
            # their value at the current bit position (j) but it looks like j  is already at 1
            # when it hits this if; though I expected it to still be at 0.
            print(input)
            print(j)
            for each in input:
                print(each,each[j])
                if each[j] != 1:
                    a=input.remove(each)
            part_2(a)

            # input = [item for item in input if int(input[i][j]) ==1]
            print(input)
            # epsilon[j]=0
        elif zeros > ones:
            for each in input:
                print(each,each[j])
                if each[j] != 0:
                    input.remove(each)
            # epsilon[j]=1

        zeros = ones = 0

    # my dumbass approach to converting a list of 0's and 1's to decimal
    gamma_dec = 0
    epsilon_dec = 0
    j=len(gamma)-1
    for i in range(0,len(gamma)):
        gamma_dec += int(gamma[i])*(2**j)
        epsilon_dec += epsilon[i]*(2**j)
        j-=1

    return gamma_dec*epsilon_dec


# print("Part One : "+ str(part_1(input)))



print("Part Two : "+ str(part_2(input)))
