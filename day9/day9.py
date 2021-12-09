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

def find_lowest(data, tran_data):
    count = []
    for r_index, row in enumerate(data):
        for c_index, cur_num in enumerate(row):
            row_check = check_row(c_index, row)
            column_check = check_row(r_index, tran_data[c_index])
            if row_check and column_check:
                if cur_num == '9':
                    print(r_index,c_index) 
                count.append(cur_num)
    return count

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
with open(file_name) as f:
    data = f.read().splitlines()
    split_data = [list(row) for row in data]
    transformed_data = list(zip(*data))
    count = find_lowest(split_data,transformed_data)
    int_count = [int(i) +1 for i in count] 
    print(sum(int_count))

    f.close()


# ## part 2

