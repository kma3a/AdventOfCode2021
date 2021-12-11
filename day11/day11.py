import sys
import math
check_argv = len(sys.argv)
default = 'test'
input = sys.argv[1] if check_argv>1 else default
file_name = f'{input}.txt'
steps = int(sys.argv[2]) if check_argv>2 else 100 


def go_right(cord):
    mod = cord.copy()
    mod[1] = cord[1]+1
    return mod

# print('go_right')
# print(go_right([1,0]) == [1,1])
# print(go_right([1,4]) == [1,5])


def go_dag_right_up(cord):
    mod = cord.copy()
    mod[1] = cord[1]+1
    mod[0] = cord[0]-1
    return mod

# print('go_dag_right_up')
# print(go_dag_right_up([1,0]) == [0,1])
# print(go_dag_right_up([1,4]) == [0,5])

def go_dag_right_down(cord):
    mod = cord.copy()
    mod[1] = cord[1]+1
    mod[0] = cord[0]+1
    return mod

# print('go_dag_right_down')
# print(go_dag_right_down([1,0]) == [2,1])
# print(go_dag_right_down([1,4]) == [2,5])

def go_left(cord):
    mod = cord.copy()
    mod[1] = cord[1]-1
    return mod

# print('go_left')
# print(go_left([1,2]) == [1,1])
# print(go_left([1,4]) == [1,3])

def go_dag_left_up(cord):
    mod = cord.copy()
    mod[1] = cord[1]-1
    mod[0] = cord[0]-1
    return mod

# print('go_dag_left_up')
# print(go_dag_left_up([1,2]) == [0,1])
# print(go_dag_left_up([1,4]) == [0,3])

def go_dag_left_down(cord):
    mod = cord.copy()
    mod[1] = cord[1]-1
    mod[0] = cord[0]+1
    return mod

# print('go_dag_left_down')
# print(go_dag_left_down([1,2]) == [2,1])
# print(go_dag_left_down([1,4]) == [2,3])

def go_up(cord):
    mod = cord.copy()
    mod[0] = cord[0]-1
    return mod

# print('go_up')
# print(go_up([1,2]) == [0,2])
# print(go_up([2,4]) == [1,4])

def go_down(cord):
    mod = cord.copy()
    mod[0] = cord[0]+1
    return mod

# print('go_down')
# print(go_down([1,2]) == [2,2])
# print(go_down([2,4]) == [3,4])

direction = {
        'right': go_right,
        'left': go_left,
        'up': go_up,
        'down': go_down,
        'drup': go_dag_right_up,
        'drdown': go_dag_right_down,
        'dlup': go_dag_left_up,
        'dldown': go_dag_left_down
    }

def check_flash(level):
    return 9 < level

# print('check_flash')
# print(check_flash(10)== True)
# print(check_flash(9)== False)
# print(check_flash(0)== False)
# print(check_flash(3)== False)

def in_boundary(cord, row_max, column_max):
    negative = cord[0] > -1 and cord[1] > -1
    above = cord[0] < row_max and cord[1] < column_max 
    return negative and  above

# print(in_boundary([0,-1],3,4)==False)
# print(in_boundary([-1,3],3,4)==False)
# print(in_boundary([2,4],3,4)==False)
# print(in_boundary([3,2],3,4)==False)
# print(in_boundary([1,1],3,4)==True)



def step(cur_data):
    flash = []
    def inc_data(data):
        for r_in, row in enumerate(data):
            for c_in, col in enumerate(row):
                new_level = int(col) + 1
                data[r_in][c_in]= new_level
                if check_flash(new_level):
                    flash.append([r_in,c_in]) 
        return data
    # print('inc_data test')
    # test1_data = [['0','0','0','0','0'],['0','8','8','8','0'],['0','8','0','8','0'],['0','8','8','8','0'],['0','0','0','0','0']]
    # finish1_data = [[1,1,1,1,1],[1,9,9,9,1],[1,9,1,9,1],[1,9,9,9,1],[1,1,1,1,1]]
    # print(inc_data(test1_data)== finish1_data)
    # print('flash test')
    # print(flash == [[1,1],[1,2],[1,3],[2,1],[2,3],[3,1],[3,2],[3,3]])
    # test2_data = [[3,4,5,4,3],[4,0,0,0,4],[5,0,0,0,5],[4,0,0,0,4],[3,4,5,4,3]]
    # finish2_data = [[4,5,6,5,4],[5,1,1,1,5],[6,1,1,1,6],[5,1,1,1,5],[4,5,6,5,4]]
    # flash = []
    # print(inc_data(test2_data)== finish2_data)
    # print('flash')
    # print(flash ==[])


    def flash_change(data):
        copy_data = data.copy()
        for index, cord in enumerate(flash):
            for key in direction.keys():
                check_cord = direction[key](cord)
                if in_boundary(check_cord, len(copy_data), len(copy_data[0])):
                    new_level = copy_data[check_cord[0]][check_cord[1]]+1
                    copy_data[check_cord[0]][check_cord[1]] = new_level
                    if check_flash(new_level) and not check_cord in flash:
                        flash.append(check_cord)
        for cord in flash:
            if copy_data[cord[0]][cord[1]] >=9:
                copy_data[cord[0]][cord[1]] = 0 
        return copy_data 
    # print('flash test')
    # flash = [[1,1],[1,2],[1,3],[2,1],[2,3],[3,1],[3,2],[3,3]]
    # test1_data = [[2,2,2,2,2],[2,10,10,10,2],[2,10,2,10,2],[2,10,10,10,2],[2,2,2,2,2]]
    # step1_data = [[3,4,5,4,3],[4,0,0,0,4],[5,0,0,0,5],[4,0,0,0,4],[3,4,5,4,3]]
    # print(flash_change(test1_data) == step1_data)

    cur_data = inc_data(cur_data)
    final_data = flash_change(cur_data)
    flash_count = len(flash)
    return [final_data, flash_count]
# print('step test')
# test1_data = [['1','1','1','1','1'],['1','9','9','9','1'],['1','9','1','9','1'],['1','9','9','9','1'],['1','1','1','1','1']]
# finish1_data = [[3,4,5,4,3],[4,0,0,0,4],[5,0,0,0,5],[4,0,0,0,4],[3,4,5,4,3]]
# test1_final = step(test1_data)
# print(test1_final == finish1_data)
# finish2_data = [[4,5,6,5,4],[5,1,1,1,5],[6,1,1,1,6],[5,1,1,1,5],[4,5,6,5,4]]
# print(step(test1_final)== finish2_data)
                
### part 1
with open(file_name) as f:
    data = f.read().splitlines()
    split_data = [list(row) for row in data]
    step_count =0 
    flash_count =0 
    while step_count < steps:
       step_data = step(split_data)
       split_data = step_data[0]
       flash_count += step_data[1]
       step_count+=1
    print(flash_count)
    f.close()


# ## part 2
# with open(file_name) as f:
#     scores = []
#     data = f.read().splitlines()
#     f.close())

