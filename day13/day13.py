import sys
from pprint import pprint
check_argv = len(sys.argv)
default = 'test'
input = sys.argv[1] if check_argv>1 else default
file_name = f'{input}.txt'
dot = '#'
empty = '.'
                
### part 1

def create_board(data):
    split_data = [ i.split(",") for i in data]
    tran_data = list(zip(*split_data))
    y_val = [int(i) for i in list(tran_data[0])]
    y_val.sort()
    highest_y = y_val[-1:][0]+1

    x_val = [int(i) for i in list(tran_data[1])]
    x_val.sort()
    highest_x = x_val[-1:][0] + 1
    board = [[empty]*highest_y for i in range(highest_x)]

    for cord in split_data:
        x_cord = int(cord[1])
        y_cord = int(cord[0])
        board[x_cord][y_cord] = dot

    return board


# test = ['1,3','0,2','3,4']
# test_board = create_board(test)
# print(test_board)
# final = [[empty,empty,empty,empty],[empty,empty,empty,empty],[dot,empty,empty,empty],[empty,dot,empty,empty],[empty,empty,empty,dot]]
# print(test_board == final)


def update_board(cur, diff):
        for r_in, r_val in enumerate(diff):
                for c_in, c_val in enumerate(r_val):
                    if c_val == dot :
                        cur[r_in][c_in] = dot
        return cur


def fold_board(board, instructions):
    copy_board = board.copy()
    for cur_inst in instructions:
        space_neg_index = ~cur_inst[::-1].index(' ')+1
        value = cur_inst[space_neg_index:].split('=')
        if value[0] == 'y':
            kept_board = copy_board[:int(value[1])][::-1]
            neg_ind = 0 - len(copy_board) + int(value[1]) +1
            change_board = copy_board[neg_ind:]
            copy_board = update_board(kept_board, change_board)[::-1]
        else:
            kept_board = [row[:int(value[1])][::-1] for row in copy_board]
            neg_ind = 0 - len(copy_board[0]) + int(value[1]) +1
            change_board = [row[neg_ind:] for row in copy_board]
            copy_board = update_board(kept_board, change_board) 
            copy_board = [row[::-1] for row in copy_board] 
    return copy_board
            


# board = [[empty,empty,dot,empty,empty],[empty,empty,empty,dot,empty],[empty,empty,empty,empty,empty],[empty,empty,empty,empty,dot],[dot,empty,empty,empty,empty]]
# test_i = ['fold along y=2']
# test_board = fold_board(board, test_i)
# final = [[dot,empty,dot,empty,empty],[empty,empty,empty,dot,dot]]
# print(test_board == final)

# board = [[empty,dot,empty,empty,empty],[empty,empty,empty,empty,dot],[empty,empty,empty,empty,empty],[empty,empty,empty,dot,empty],[dot,empty,empty,empty,empty]]
# test_i = ['fold along x=2']
# test_board = fold_board(board, test_i)
# final = [[empty,dot],[dot,empty],[empty,empty], [empty,dot],[dot,empty]]
# print(test_board == final)

# board = [[empty,dot,empty,empty,empty],[empty,empty,empty,empty,dot],[empty,empty,empty,empty,empty],[empty,empty,empty,empty,dot],[dot,empty,empty,empty,empty]]
# test_i = ['fold along x=2','fold along y=2']
# test_board = fold_board(board, test_i)
# final = [[dot,dot],[dot,empty]]
# print(test_board)
# print(test_board == final)

# board = [[empty,dot,empty,empty,empty],[empty,empty,empty,empty,dot],[empty,empty,empty,empty,dot],[empty,empty,empty,empty,empty],[dot,empty,empty,empty,empty]]
# test_i = ['fold along y=3']
# test_board = fold_board(board, test_i)
# final = [[empty,dot,empty,empty,empty],[empty,empty,empty,empty,dot],[dot,empty,empty,empty,dot]]
# print(test_board)
# print(test_board == final)

# board = [[empty,dot,empty,empty],[empty,empty,empty,dot],[empty,empty,empty,empty],[empty,empty,empty,empty],[dot,empty,empty,dot]]
# test_i = ['fold along x=2']
# test_board = fold_board(board, test_i)
# final = [[empty,dot],[empty,dot],[empty,empty], [empty,empty],[dot,dot]]
# print(test_board == final)


# with open(file_name) as f:
#     data = f.read().splitlines()
#     space_index = data.index('')
#     space_neg_index = ~data[::-1].index('')+1
#     instructions = data[:space_index]
#     folds = [data[space_neg_index:][0]]
#     board = create_board(instructions)
#     new_board = fold_board(board, folds)
#     join = [item for sublist in new_board for item in sublist]
#     print(join.count(dot))
#     f.close()


# ## part 2
with open(file_name) as f:
    data = f.read().splitlines()
    space_index = data.index('')
    space_neg_index = ~data[::-1].index('')+1
    instructions = data[:space_index]
    folds = data[space_neg_index:]
    board = create_board(instructions)
    new_board = fold_board(board, folds)
    print(*new_board, sep='\n')
    join = [item for sublist in new_board for item in sublist]
    print(join.count(dot))
    f.close()
