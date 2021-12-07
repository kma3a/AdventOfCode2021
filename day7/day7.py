import sys
import math
check_argv = len(sys.argv)
default = 'test'
input = sys.argv[1] if check_argv>1 else default
file_name = f'{input}.txt'

def calculate_fuel(data, position):
    single_data = list(set(data))
    count = 0
    for crab in single_data:
        crab_num = data.count(crab)
        count += (abs(crab - position)) * crab_num
    return count



# print(calculate_fuel([1,2,3,15], 2) == 15)
# print(calculate_fuel([1,2,3,15,15], 2) == 28)
# print(calculate_fuel([16,1,2,0,4,2,7,1,2,14], 2) == 37)
# print(calculate_fuel([16,1,2,0,4,2,7,1,2,14], 1) == 41)

### part 1
with open(file_name) as f:
    data = [ int(item) for item in f.read().split(',')]
    data.sort()
    median = data[int(len(data)/2)]
    print(calculate_fuel(data, median))
    f.close()


# ## part 2
# with open(file_name) as f:
#     f.close()

