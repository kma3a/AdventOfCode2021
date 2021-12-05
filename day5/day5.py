import sys
import re
check_argv = len(sys.argv)-1
default = 'test'
input = sys.argv[1] if check_argv==1 else default
file_name = f'{input}.txt'



def mark_num(data, call_num):
    new_data=[]
    for row in data:
        row = row.split(' ')
        row = ['X' if item == call_num else item for item in row ]
        row = ' '.join(row)
        new_data.append(row)
    return new_data

def check_win(current_board):
    win_condition='XXXXX'
    board=",".join(current_board).replace(" ", "").split(',')
    trans_board = re.sub(' +', ' ', " ".join(current_board)).lstrip().split(' ')
    trans_board = [trans_board[i:i + 5] for i in range(0, len(trans_board), 5)] 
    trans_board = ["".join(index) for index in list(zip(*trans_board))]
    return True if win_condition in board or win_condition in trans_board else False

def sum_unmarked(board):
    board = re.sub(' +', ' ',' '.join(board).replace("X",'')).split(' ')
    sum_list = [ int(board[i]) if board[i] != '' else 0 for i in range(0, len(board))]
    return sum(sum_list)

### part 1
# def get_win_index(boards):
#     win_index = -1
#     for index, current_board in enumerate(boards):
#         if check_win(current_board): 
#             win_index = index
#             break
#     return win_index
# with open(file_name) as f:
#     data = list(filter(('').__ne__, f.read().splitlines()))
#     call_num = data.pop(0).split(',')
#     boards=[data[i:i + 5] for i in range(0, len(data), 5)] 
#     winning_board = -1
#     index=0
#     while index<len(call_num)-1:
#         data = mark_num(data, call_num[index])
#         boards = [data[i:i + 5] for i in range(0, len(data), 5)]
#         if index > 4:
#             winning_board = get_win_index(boards)
#         if winning_board != -1:
#             break
#         index+=1
#     sum = sum_unmarked(boards[winning_board])
#     print(int(call_num[index])*sum)
#     f.close()


## part 2

def get_losing_boards(boards, losing_boards):
    for index in losing_boards:
        current_board = boards[index]
        if check_win(current_board): 
            losing_boards.remove(index)
        if len(losing_boards)==0:
            break
    return losing_boards

with open(file_name) as f:
    data = list(filter(('').__ne__, f.read().splitlines()))
    call_num = data.pop(0).split(',')
    start_boards=[data[i:i + 5] for i in range(0, len(data), 5)] 
    losing_boards = list(range(0, len(start_boards)))
    last_board = -1
    index=0
    while index<len(call_num)-1:
        data = mark_num(data, call_num[index])
        boards = [data[i:i + 5] for i in range(0, len(data), 5)]
        if index > 4:
            losing_boards = get_losing_boards(boards, losing_boards)
        if len(losing_boards) == 1:
           last_board = losing_boards[0] 
        if last_board != -1 and len(losing_boards) == 0:
            break
        index+=1
    sum = sum_unmarked(boards[last_board])
    print(last_board)
    print(call_num[index])
    print(int(call_num[index])*sum)
    f.close()