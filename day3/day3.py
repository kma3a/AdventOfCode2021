import sys
check_argv = len(sys.argv)-1
default = 'test'
input = sys.argv[1] if check_argv==1 else default
file_name = f'{input}.txt'

### part 1
# with open(file_name) as f:
#     data = f.read().splitlines()
#     gamma=[]
#     epsilon=[]
#     tran_data = list(zip(*data))
#     for data_set in tran_data:
#         if data_set.count('0') > len(data_set)/2:
#             gamma.append('0')
#             epsilon.append('1')
#         else:
#             gamma.append('1')
#             epsilon.append('0')
#     gamma_num = int("".join(gamma),2) 
#     epsilon_num = int("".join(epsilon),2) 
#     print(gamma_num*epsilon_num)
#     f.close()


## part 2


def removeData(data, remove, index):
    array =[]
    for binary in data:
        if binary[index] != remove:
            array.append(binary)
    return array

def getData(data, first, second):
    index=0
    while len(data) > 1:
        remove = first
        tran_data = list(zip(*data))
        if tran_data[index].count('0') > len(data)/2:
            remove = second
        data = removeData(data, remove, index)
        index+=1
    return int(data[0],2)

with open(file_name) as f:
    data = f.read().splitlines()
    oxygen = getData(data, '0', '1')
    co = getData(data, '1', '0')
    print(oxygen*co)
    f.close()