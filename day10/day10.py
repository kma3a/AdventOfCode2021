import sys
import math
check_argv = len(sys.argv)
default = 'test'
input = sys.argv[1] if check_argv>1 else default
file_name = f'{input}.txt'

def check_row(index, row):
    previous = index - 1 if index != 0 else None
    after = index + 1 if index != len(row) -1 else None
    check_p = False  if previous != None and row[index] >= row[previous] else True
    check_a = False  if after != None and row[index] >= row[after] else True
    return check_p and check_a

# print(check_row(1,[2,0,1]) == True)
# print(check_row(0,[2,0,1]) == False)
# print(check_row(2,[2,0,1]) == False)
# print(check_row(3,[2,0,1,4]) == False)
# print(check_row(18,[8,6,7,9,8,7,6,4,2,3,4,5,6,7,8,9,9,8,1]) == True)
# print(check_row(16,[8,6,7,9,8,7,6,4,2,3,4,5,6,7,8,9,9,9,1]) == False)

# def find_lowest(data, tran_data):
#     count = []
#     for r_index, row in enumerate(data):
#         for c_index, cur_num in enumerate(row):
#             row_check = check_row(c_index, row)
#             column_check = check_row(r_index, tran_data[c_index])
#             if row_check and column_check:
#                 count.append(cur_num)
#     return count

# test1_data =[[1,2,3],[2,7,4],[3,8,5]] 
# test1_tran = list(zip(*test1_data))
# print(find_lowest(test1_data, test1_tran) == [1])
# test2_data =[[1,2,3,5],[2,7,4,3],[3,8,5,1]] 
# test2_tran = list(zip(*test2_data))
# print(find_lowest(test2_data, test2_tran) == [1,1])
# test3_data =[[1,2,3,5],[2,7,2,3],[3,8,5,1]] 
# test3_tran = list(zip(*test3_data))
# print(find_lowest(test3_data, test3_tran) == [1,2,1])

### part 1
# with open(file_name) as f:
#     data = f.read().splitlines()
#     split_data = [list(row) for row in data]
#     transformed_data = list(zip(*data))
#     count = find_lowest(split_data,transformed_data)
#     int_count = [int(i) +1 for i in count] 
#     print(sum(int_count))

#     f.close()

# def count_row(start_value, row):
    

# print(count_row(0, [2,1,9]) == 2)
# print(count_row(0, [3,9,8]) == 1)
# print(count_row(0, [3,9,8]) == 1)
def go_right(cord):
    mod = cord.copy()
    mod[1] = cord[1]+1
    return mod

# print(go_right([1,0]) == [1,1])
# print(go_right([1,4]) == [1,5])

def go_left(cord):
    mod = cord.copy()
    mod[1] = cord[1]-1
    return mod

# print(go_left([1,2]) == [1,1])
# print(go_left([1,4]) == [1,3])

def go_up(cord):
    mod = cord.copy()
    mod[0] = cord[0]-1
    return mod

# print(go_up([1,2]) == [0,2])
# print(go_up([2,4]) == [1,4])

def go_down(cord):
    mod = cord.copy()
    mod[0] = cord[0]+1
    return mod

# print(go_down([1,2]) == [2,2])
# print(go_down([2,4]) == [3,4])

def in_boundary(cord, row_max, column_max):
    negative = cord[0] > -1 and cord[1] > -1
    above = cord[0] < row_max and cord[1] < column_max 
    return negative and  above

# print(in_boundary([0,-1],3,4)==False)
# print(in_boundary([-1,3],3,4)==False)
# print(in_boundary([2,4],3,4)==False)
# print(in_boundary([3,2],3,4)==False)
# print(in_boundary([1,1],3,4)==True)

def get_basin_size(cord, data):
    # transformed_data = list(zip(*data))
    direction = {
        'right': go_right,
        'left': go_left,
        'up': go_up,
        'down': go_down,
    }
    keys = list(direction.keys())
    count = [cord] 
    checked_coord = [cord]
    finished =False
    count_index = 0
    while count_index < len(checked_coord):
        curr_cord = checked_coord[count_index]
        for index, key in enumerate(keys):
            checking = direction[key](curr_cord) 
            if in_boundary(checking, len(data), len(data[0])) and int(data[checking[0]][checking[1]]) != 9 and not checking in count: 
                count.append(checking)
            if index == len(keys)-1:
                break
            checking= direction[keys[index+1]](curr_cord) 
        if len(checked_coord) != len(count) and count_index < len(count):
            count_index+=1
            checked_coord.append(count[count_index]) 
        else:
            break
    return len(count)

    
# test1_data =[[2,1,9],[3,9,8],[9,8,5]]
# test_return = get_basin_size([0,1], test1_data)
# print(test_return == 3)
# test_return = get_basin_size([1,2], [[2,1,9],[3,9,8],[9,8,5],[9,2,4]])
# print(test_return == 5)



def find_lowest(data, tran_data):
    count = []
    for r_index, row in enumerate(data):
        for c_index, cur_num in enumerate(row):
            row_check = check_row(c_index, row)
            column_check = check_row(r_index, tran_data[c_index])
            if row_check and column_check:
                count.append([r_index, c_index])
    return count

# test1_data =[[1,2,3],[2,7,4],[3,8,5]] 
# test1_tran = list(zip(*test1_data))
# test_count = find_lowest(test1_data, test1_tran) 
# print(test_count == [[0,0]])
# test2_data =[[1,2,3,5],[2,7,4,3],[3,8,5,1]] 
# test2_tran = list(zip(*test2_data))
# test_count = find_lowest(test2_data, test2_tran) 
# print(test_count == [[0,0],[2,3]])
# test3_data =[[1,2,3,5],[2,7,2,3],[3,8,5,1]] 
# test3_tran = list(zip(*test3_data))
# test_count = find_lowest(test3_data, test3_tran)
# print( test_count == [[0,0],[1,2],[2,3]])


# ## part 2
with open(file_name) as f:
    data = f.read().splitlines()
    split_data = [list(row) for row in data]
    transformed_data = list(zip(*data))
    count = find_lowest(split_data,transformed_data)
    basin_count = []
    for cord in count:
       basin_count.append(get_basin_size(cord, data))
    basin_count.sort()
    print(math.prod(basin_count[-3:]))

    # tests
    # print(split_data)
    # print(get_basin_size([0,1], split_data)== 3)
    # print(get_basin_size([0,9], split_data)== 9)
    f.close()

