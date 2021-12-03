# # part 1
# def createDic(length):
#     start ={}
#     index=0
#     while index<length:
#         start[index]=0
#         index+=1
#     return start

# def getGamma(countZero, length):
#     gamma=[]
#     for key in countZero.keys(): 
#         if countZero[key] > length/2:
#             gamma.append('0')
#         else:
#             gamma.append('1')
#     return int("".join(gamma),2)


# def getEpsilon(countZero, length):
#     epsilon=[]
#     for key in countZero.keys(): 
#         if countZero[key] < length/2:
#             epsilon.append('0')
#         else:
#             epsilon.append('1')
#     return int("".join(epsilon),2)


# with open('input.txt') as f:
#     data = f.read().splitlines()
#     countZero = createDic(len(data[0]))
#     for line in data:
#         for key in countZero.keys():
#             if int(line[int(key)]) == 0:
#                 countZero[key]+=1
#     gamma = getGamma(countZero, len(data))
#     epsilon = getEpsilon(countZero, len(data))
#     print(gamma*epsilon)

#     f.close()


## part 2

def getZeroCount(data, position):
    count=0
    for binary in data:
        if binary[position] == '0':
            count+=1
    return count

def removeData(data, remove, index):
    array =[]
    for binary in data:
        if binary[index] != remove:
            array.append(binary)
    return array

def getOxygen(data):
    index=0
    while len(data) > 1:
        remove = '0'
        zero_count = getZeroCount(data, index)
        if zero_count > len(data)/2:
            remove = '1'
        data = removeData(data, remove, index)
        index+=1
    return int(data[0],2)

def getCO(data):
    index=0
    while len(data) > 1:
        remove = '1'
        zero_count = getZeroCount(data, index)
        if zero_count > len(data)/2:
            remove = '0'
        data = removeData(data, remove, index)
        index+=1
    return int(data[0],2)





with open('input.txt') as f:
    data = f.read().splitlines()
    oxygen = getOxygen(data)
    co = getCO(data)
    print(oxygen*co)
    f.close()