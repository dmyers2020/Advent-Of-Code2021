# Advent of code Year 2021 Day 4 solution
# Author = David Myers
# Date = December 2020
import pandas as pd
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = list(input_file.readlines())
    # print(input)
# wrangling
nums_called = input[0]
nums_called = nums_called.split(",")
list(map(int ,nums_called))
# print(len(nums_called))

boards = input[1:]

for each in boards:
    if each == '\n':
        del (boards[boards.index(each)])


boards2 = [each.rstrip('\n').split(' ') for each in boards]


for list in boards2:
    for each in list:
        if each == '':
            del (list[list.index(each)])

# print(boards2)
boards3 = [[int(s) for s in sublist] for sublist in boards2]

boards4 = []
for i in range(0,len(boards3),5):
    boards4.append(boards3[i:i+5])


# boards5 = []
# for board in boards4:
#     boards5.append(pd.DataFrame(board))


'''
part 2: modify part 1 to eliminate the board index for list of boards if bingo is found.
'''
# board_list = {i for i in range(0,len(boards4))}
# board_list2 =[]
# print(board_list)

# bingo = 0
k =0
while len(boards4) > 1:
    for num in nums_called:
        if len(boards4) == 1:
            break
        for board in boards4:
            for row in board:
                for col in row:
                    if col == int(num):
                        # print(num, board, boards3.index(board), row, board.index(row), col, row.index(col))
                        # list_of_matches.append([boards3.index(board),board.index(row),row.index(col)])
                        boards4[boards4.index(board)][board.index(row)][row.index(col)] = 'm'
                        if row.count('m')==5:
                            k+=1
                            print(f'bingo ROW on board #: {boards4.index(board)} \n last number called: {num} \n\n {k}')
                            bingo_board = board.copy()
                            last_num_called = num
                            # board_list.discard(boards4.index(board))
                            # board_list2.append(boards4.index(board))
                            del boards4[boards4.index(board)]
                            print(boards4)
                            break

                        for i in range(0,5):
                            col_match_count = 0
                            for j in range(0,5):
                                # print(f' board i j: {board[i][j]}')
                                if board[j][i] == 'm':
                                    col_match_count +=1
                                    # print(col_match_count)
                                if col_match_count == 5:
                                    k+=1
                                    print(f'bingo COLUMN on board #: {boards4.index(board)} \n last number called: {num} \n\n {k} ')
                                    # for row in board:
                                    #     print(row)
                                    bingo_board = board.copy()
                                    last_num_called = num
                                    # board_list.discard(int(boards4.index(board)))
                                    # board_list2.append(boards4.index(board))
                                    del boards4[boards4.index(board)]
                                    break
                            else:
                                continue
                                break

                    # else:
                    #     continue
                    #     break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break

# board_list2 = set(board_list2)


# print(f' the last board is: {bingo_board}')
'''
9744 from board 0 is too low.
'''
# print(boards4[73])
print(boards4)
score = int(0)
for row in bingo_board:
    print(row)
    for value in row:
        if value != 'm':
            score += int(value)

print(f' the sum of remaining numbers on the card: {score} \n the last number called: {last_num_called}')
final_score= int(score)*int(last_num_called)


print("Part One : "+ str(final_score))



print("Part Two : "+ str(None))
