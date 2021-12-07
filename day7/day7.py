import sys
import math
check_argv = len(sys.argv)
default = 'test'
input = sys.argv[1] if check_argv>1 else default
file_name = f'{input}.txt'

### part 1
# def calculate_fuel(data, position):
#     single_data = list(set(data))
#     count = 0
#     for crab in single_data:
#         crab_num = data.count(crab)
#         count += (abs(crab - position)) * crab_num
#     return count



# print(calculate_fuel([1,2,3,15], 2) == 15)
# print(calculate_fuel([1,2,3,15,15], 2) == 28)
# print(calculate_fuel([16,1,2,0,4,2,7,1,2,14], 2) == 37)
# print(calculate_fuel([16,1,2,0,4,2,7,1,2,14], 1) == 41)


# with open(file_name) as f:
#     data = [ int(item) for item in f.read().split(',')]
#     data.sort()
#     median = data[int(len(data)/2)]
#     print(calculate_fuel(data, median))
#     f.close()


# ## part 2
def calculate_move(crab_pos, pos):
    pos_diff = abs(crab_pos - pos)
    return sum(i+1 for i in range(0, pos_diff))

# print(calculate_move(1,1) == 0)
# print(calculate_move(4,5) == 1)
# print(calculate_move(7,5) == 3)
# print(calculate_move(2,5) == 6)
# print(calculate_move(1,5) == 10)
# print(calculate_move(14,5) == 45)
# print(calculate_move(16,5) == 66)

def calculate_fuel(data, position):
    single_data = list(set(data))
    count = 0
    for crab in single_data:
        crab_num = data.count(crab)
        count += (calculate_move(crab, position)) * crab_num
    return count

# print(calculate_fuel([1,2,3], 2) == 2)
# print(calculate_fuel([16,1,2,0,4,2,7,1,2,14], 2) == 206)
# print(calculate_fuel([16,1,2,0,4,2,7,1,2,14], 5) == 168)


with open(file_name) as f:
    data = [ int(item) for item in f.read().split(',')]
    data.sort()
    mean = round(sum(data)/len(data))
    position = mean-1
    shortest = calculate_fuel(data, mean-1)
    for index in range(mean-1, mean+1):
        fuel = calculate_fuel(data, index)
        if shortest > fuel:
            position = index
            shortest = fuel
    print(position)
    print(shortest)
    f.close()

