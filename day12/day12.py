import sys
import math
check_argv = len(sys.argv)
default = 'test'
input = sys.argv[1] if check_argv>1 else default
file_name = f'{input}.txt'
                
### part 1

def draw_connections(data):
    connections = {}
    def add_con(first,second):
        if not first in connections.keys():
            connections[first] = [second]
        else:
           connections[first].append(second) 

    for row in data:
        has_start_or_fin = False
        first= row[0]
        second = row[1]
        if 'start' in row or 'end' in row:
            has_start_or_fin = True 
        if 'start' in row and first !='start':
            first=row[1]
            second=row[0]
        elif 'end' in row and second !='end':
            first=row[1]
            second=row[2]
        add_con(first,second) 
        if not has_start_or_fin:
            add_con(second,first)

    return connections


# test = [['start', 'a'], ['start','B'],['B','c'],['a','end'],['c','end']]
# test_r = draw_connections(test) 
# print(test_r)
# print(test_r['start']==['a','B'])
# print(test_r['a']==['end'])
# print(test_r['B']==['c'])
# print(test_r['c']==['B','end'])

def get_paths(data):
    





test = [['start', 'a'], ['a','end'],]
test_r = draw_connections(test) 
test_f = get_paths(test_r) 
paths=[['start', 'a','end']]
print(test_f == paths )


# with open(file_name) as f:
#     data = f.read().splitlines()
#     split_data = [row.split('-') for row in data]
#     con = draw_connections(split_data)
#     print(con)
#     f.close()


# ## part 2
# with open(file_name) as f:
#     data = f.read().splitlines()
#     f.close()
