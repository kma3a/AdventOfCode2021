import sys
import math
check_argv = len(sys.argv)-1
day_default = 18
default = 'test'
input = sys.argv[1] if check_argv==2 else default
day_set = int(sys.argv[2]) if check_argv==2 else day_default
file_name = f'{input}.txt'


### part 1
# def change_time(days):
#     if days == 0:
#         return 6
#     return days-1
    

# print(change_time(2) == 1)
# print(change_time(0) == 6)
# print(change_time(6) == 5)

# with open(file_name) as f:
#     data = [ int(item) for item in f.read().split(',')]
#     day_count = 0
#     while day_count < day_set:
#         zero_count = data.count(0)
#         data = [change_time(fish) for fish in data]
#         [data.append(8) for index in range(0, zero_count) ]
#         day_count+=1
#     print(len(data))
#     f.close()


# ## part 2
with open(file_name) as f:
    data = [ int(item) for item in f.read().split(',')]
    days_list = ['8','7','6','5','4','3','2','1','0']
    fish_hash = {
        '0': data.count(0),
        '1': data.count(1),
        '2': data.count(2),
        '3': data.count(3),
        '4': data.count(4),
        '5': data.count(5),
        '6': data.count(6),
        '7': data.count(7),
        '8': data.count(8),
    }
    day_count = 0
    while day_count < day_set:
        new_hash = {
            '0': 0,
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
        }
        for index, item in enumerate(days_list):
            if index == len(days_list)-1:
                new_hash['6'] += fish_hash[item]
                new_hash['8'] += fish_hash[item]
            else:
                new_hash[days_list[index+1]] += fish_hash[item]
        fish_hash = new_hash
        day_count+=1
    print(sum(fish_hash.values()))


    f.close()

