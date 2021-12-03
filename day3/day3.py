import sys
file_name = f'{sys.argv[1]}.txt'

def getZeroCount(data, position):
    count=0
    for binary in data:
        if binary[position] == '0':
            count+=1
    return count

### part 1
with open(file_name) as f:
    data = f.read().splitlines()
    gamma=[]
    epsilon=[]
    index=0
    while index < len(data[0]):
        if getZeroCount(data, index) > len(data)/2:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')
        index+=1
    gamma_num = int("".join(gamma),2) 
    epsilon_num = int("".join(epsilon),2) 
    print(gamma_num*epsilon_num)

    f.close()


## part 2


# def removeData(data, remove, index):
#     array =[]
#     for binary in data:
#         if binary[index] != remove:
#             array.append(binary)
#     return array

# def getOxygen(data):
#     index=0
#     while len(data) > 1:
#         remove = '0'
#         zero_count = getZeroCount(data, index)
#         if zero_count > len(data)/2:
#             remove = '1'
#         data = removeData(data, remove, index)
#         index+=1
#     return int(data[0],2)

# def getCO(data):
#     index=0
#     while len(data) > 1:
#         remove = '1'
#         zero_count = getZeroCount(data, index)
#         if zero_count > len(data)/2:
#             remove = '0'
#         data = removeData(data, remove, index)
#         index+=1
#     return int(data[0],2)





# with open(file_name) as f:
#     data = f.read().splitlines()
#     oxygen = getOxygen(data)
#     co = getCO(data)
#     print(oxygen*co)
#     f.close()