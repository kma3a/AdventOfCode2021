import sys

check_argv = len(sys.argv)-1
default = 'test'
input = sys.argv[1] if check_argv==1 else default
file_name = f'{input}.txt'

# with open(file_name) as f:
#     data = f.read().splitlines()
#     positive = 0
#     for previous_num, current_num in zip(data[::],data[1::]):
#         if int(current_num) > int(previous_num):
#             positive+=1
#     f.close()
#     print(positive)

# ## part2

with open(file_name) as f:
    data = f.read().splitlines()
    positive = -1
    previous_sum = 0
    for num_one, num_two, num_thr in zip(data[::],data[1::], data[2::]):
        current_sum = int(num_one) + int(num_two) + int(num_thr)
        if current_sum > previous_sum:
            positive+=1
        previous_sum=current_sum
    f.close()
    print(positive)