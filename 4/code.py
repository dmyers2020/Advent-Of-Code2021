# Advent of code Year 2021 Day 4 solution
# Author = https://github.com/luisbc92 | https://www.reddit.com/user/TacosAlPastor92/
# Collaborator = David Myers
# Date = December 2020
import numpy as np

input = open('Advent Of Code2021/4/input.txt').read()

draw, boards = input.split('\n', 1)
draw = [int(i) for i in draw.split(',')]
boards = boards.strip().split('\n\n')

boards = [
    np.array([[int(j) for j in i.split(' ') if j != ''] for i in board.strip().split('\n')])
    for board in boards
]

def checkIfWon(board):
    for y in range(board.shape[0]):
        if np.all(board[y,:] > 100): return True

    for x in range(board.shape[1]):
        if np.all(board[:,x] > 100): return True

    return False

def result(board, num):
    return np.sum(board[board < 100]) * num

won = []
for num in draw:
    if len(boards) == 0:
        break
    for i in range(len(boards) - 1, -1, -1):
        b = boards[i]
        b[b == num] += 101
        if checkIfWon(b):
            won.append((b, num))
            boards.pop(i)


for each in won:
    print(each)

print('Part 1:' , result(*won[0]))
print('Part 2:' , result(*won[-1]))
