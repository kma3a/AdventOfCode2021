import sys
import re
check_argv = len(sys.argv)-1
default = 'test'
input = sys.argv[1] if check_argv==1 else default
file_name = f'{input}.txt'

board = []
max_values = [0,0]
def check_diagonal(start_point,end_point):
    return True if start_point[1] - start_point[0] == end_point[1] - end_point[0] or start_point[1] + start_point[0] == end_point[1] + end_point[0] else False

def create_board(x_finish, y_finish):
    index =0
    while index < x_finish+1:
        board.append([0]*(y_finish+1))
        index+=1

def mark_board(start_point,end_point):
    start = end_point  if start_point[0]>= end_point[0] and start_point[1]>= end_point[1] else start_point
    end = start_point if start != start_point else end_point
    x = start[0]
    y = start[1]
    end_x = end[0]+1 if start[0] < end[0] else end[0]-1
    end_y = end[1]+1 if start[1] < end[1] else end[1]-1
    while ((x <= end[0] and y <= end[1]) and not check_diagonal(start_point,end_point)) or (x != end_x and y != end_y):
        board[x][y]+=1
        if start[1] == end[1] and  start[0] != end[0]:
            x+=1
        elif start[0] == end[0] and  start[1] != end[1]:
            y+=1
        else:
            x+= 1 if start[0] < end[0] else -1
            y+= 1 if start[1] < end[1] else -1

def check_pairs(start_point,end_point):
    # return True if start_point[0] == end_point[0] or start_point[1] == end_point[1] or start_point[0] == end_point[0] else False
    return True if start_point[0] == end_point[0] or start_point[1] == end_point[1] or start_point[0] == end_point[0] or check_diagonal(start_point,end_point) else False

def check_max(start_point,end_point):
    max_x = end_point[0]  if start_point[0]<= end_point[0] else start_point[0]
    max_y = end_point[1]  if start_point[1]<= end_point[1] else start_point[1] 
    max_values[0] = max_x if max_x > max_values[0] else max_values[0]
    max_values[1] = max_y if max_y > max_values[1] else max_values[1]

def get_kept_data(data):
    kept_data=[]
    for line in data:
        split_line = line.split(" -> ")
        values = [ i.split(",") for i in split_line]
        values = [list(map(int, lst)) for lst in values]
        if check_pairs(values[0], values[1]):
            kept_data.append(values)
            check_max(values[0], values[1])
    return kept_data

def count_values():
    count_board = board.copy()
    count_list = [item for sublist in count_board for item in sublist if item >= 2]
    number_of_elements = len(count_list)
    return number_of_elements 




### part 1
# with open(file_name) as f:
#     data = f.read().splitlines()
#     kept= get_kept_data(data)
#     create_board(max_values[0], max_values[1])
#     for line in kept:
#         mark_board(line[0],line[1])
#     print(count_values())
#     f.close()

# print(check_pairs([0,0], [1,2]) == False)
# print(check_pairs([0,0], [0,2]) == True)
# print(check_pairs([4,2], [1,2]) == True)
# check_max([4,2], [1,2])
# print(max_values == [4,2])
# check_max([3,2], [1,9])
# print(max_values == [4,9])
# check_max([3,2], [1,9])
# print(max_values == [4,9])

# ## part 2
with open(file_name) as f:
    data = f.read().splitlines()
    kept= get_kept_data(data)
    create_board(max_values[0], max_values[1])
    for line in kept:
        mark_board(line[0],line[1])
    print(count_values())
    f.close()

# create_board(9, 9)
# mark_board([1,1], [1,3])
# # print(board)
# mark_board([9,7], [7,7])
# # print(board)
# mark_board([1,1], [3,3])
# mark_board([9,7], [7,9])

